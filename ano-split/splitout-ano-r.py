#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import fileio, lut


base_data = fileio.read_json_basis('ANO-R.1.json')

with open('splitmap-ano-r.txt', 'r') as f:
    split_data = f.readlines()[2:]

split_data = [x.strip().split() for x in split_data]
split_data = {lut.element_Z_from_sym(x[0], as_str=True): (x[1], x[2], x[3], x[4]) for x in split_data}

names = ['ANO-R0', 'ANO-R1', 'ANO-R2', 'ANO-R3']
for idx,name in enumerate(names):
    print(name) 
    new_basis = copy.deepcopy(base_data)

    for el,eldata in new_basis['elements'].items():
        el_split = split_data[el][idx]
        el_split = re.findall(r'\d+[a-z]+', el_split)
        print('  -> ', el, el_split)
        new_shells = []

        # Double and triple check
        am = [sh['angular_momentum'] for sh in eldata['electron_shells']]
        for a in am:
            assert len(a) == 1
        am = [a[0] for a in am]
            
        if len(set(am)) != len(am):
            raise RuntimeError("Duplicate AM?")

        # Now loop over the shells and trim

        old_shells = sorted(eldata.pop('electron_shells'), key=lambda x: x['angular_momentum'][0])

        for idx2,sh in enumerate(old_shells):
            if idx2 >= len(el_split):
                continue

            shell_split = el_split[idx2]
            n = int(shell_split[:-1])
            amchar = shell_split[-1]
           
            assert lut.amchar_to_int(amchar) == sh['angular_momentum'] 

            sh['coefficients'] = sh['coefficients'][:n] 
            new_shells.append(sh)

        eldata['electron_shells'] = new_shells


    fileio.write_json_basis(name + '.1.json', new_basis)
