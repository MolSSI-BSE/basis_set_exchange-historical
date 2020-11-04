#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import fileio, lut, manip

base_data = fileio.read_json_basis('ANO-RCC.1.json')

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


for name, el_cont_data in split_data.items():
    print()
    print(name) 
    new_basis = copy.deepcopy(base_data)

    missing_el = []

    for el,eldata in new_basis['elements'].items():
        if not el in el_cont_data:
            missing_el.append(el)
            continue

        el_split = el_cont_data[el]
        print('{} -> {}'.format(el, el_split))

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

    # Remove elements that aren't in the new contraction
    for el in missing_el:
        new_basis['elements'].pop(el)

    new_basis = manip.prune_basis(new_basis)
    fileio.write_json_basis(name + '.1.json', new_basis)
