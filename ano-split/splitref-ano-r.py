#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import fileio, lut
from basis_set_exchange.readers.helpers import partition_lines, parse_fixed_matrix


with open('ano-r.1.molcas', 'r') as f:
    base_data = [x.strip() for x in f.readlines()]

with open('splitmap-ano-r.txt', 'r') as f:
    split_data = f.readlines()[2:]

split_data = [x.strip().split() for x in split_data]
split_data = {lut.element_Z_from_sym(x[0], as_str=True): (x[1], x[2], x[3], x[4]) for x in split_data}


element_blocks = partition_lines(base_data, lambda x: x.startswith('/'))

names = ['ANO-R0', 'ANO-R1', 'ANO-R2', 'ANO-R3']
for idx,name in enumerate(names):
    out_lines = []

    print(name) 
    element_blocks_copy = copy.deepcopy(element_blocks)

    for block in element_blocks_copy:
        el = re.match(r'/([A-Za-z]+)\..*', block[0]).group(1)
        el = lut.element_Z_from_sym(el, as_str=True)
        el_split = split_data[el][idx]
        el_split = re.findall(r'\d+[a-z]+', el_split)
        print('  -> ', el, el_split)

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
            exponents = block[:nprim]
            block = block[nprim:]
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
