#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import fileio, lut
from basis_set_exchange.readers.helpers import partition_lines, parse_fixed_matrix, read_n_floats


with open('ano-rcc.1.molcas', 'r') as f:
    base_data = [x.strip() for x in f.readlines()]

with open('splitmap-ano-rcc.txt', 'r') as f:
    split_lines = f.readlines()

all_names = ['ANO-RCC-MB', 'ANO-RCC-VDZ', 'ANO-RCC-VDZP', 'ANO-RCC-VTZP', 'ANO-RCC-VQZP', 'ANO-RCC-VTZ']
split_data = {n: {} for n in all_names}
for l in split_lines:
    name, cont = l.split()
    el1, name1 = name.split('.')
    el2, name2, _, _, cont, _ = cont.split('.')
    assert el1 == el2
    assert name2 == 'ANO-RCC'
    assert name1 in all_names

    el = lut.element_Z_from_sym(el1, as_str=True)
    assert el not in split_data[name1]

    cont = re.findall(r'\d+[a-z]+', cont)
    split_data[name1][el] = cont


element_blocks = partition_lines(base_data, lambda x: x.startswith('/'))

for idx,name in enumerate(all_names):
    out_lines = []

    print(name) 
    element_blocks_copy = copy.deepcopy(element_blocks)

    for block in element_blocks_copy:
        el = re.match(r'/([A-Za-z]+)\..*', block[0]).group(1)
        el = lut.element_Z_from_sym(el, as_str=True)

        if el not in split_data[name]:
            continue

        el_split = split_data[name][el]
        print('  -> ', el, el_split)

        print(block)
        z, max_am = block[3].split()
        max_am = int(max_am)

        # output the comment lines
        out_lines.extend(block[:3])

        # Skip maxam line - we may need to modify it
        block = block[4:]

        shell_lines = []
        for am in range(max_am+1):
            nprim, ngen = block.pop(0).split()
            nprim = int(nprim)
            ngen = int(ngen)
            exponents, block = read_n_floats(block, nprim)
            coefficients, block = parse_fixed_matrix(block, nprim, ngen)

            if am >= len(el_split):
                break

            new_max_am = am

            shell_split = el_split[am]
            n = int(shell_split[:-1])
            #amchar = shell_split[-1]


            # n is now the new number of general contractions
            shell_lines.append("{:>5}{:>5}".format(nprim, n))
            shell_lines.extend(exponents)
            coefficients = [x[:n] for x in coefficients]
            shell_lines.extend(['    ' + '    '.join(x) for x in coefficients])

        # Now we have a new max am (maybe)
        out_lines.append('{} {}'.format(z, new_max_am))
        out_lines.extend(shell_lines)

    with open(name + '.1.molcas', 'w') as f:
        f.write('\n'.join(out_lines))
