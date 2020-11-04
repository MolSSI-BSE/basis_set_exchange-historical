#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import api, fileio, lut



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

print(split_data)

for name, el_cont_data in split_data.items():
    print(name)
    new_basis = api.get_basis(name)

    for el,eldata in new_basis['elements'].items():
        el_split = el_cont_data[el]

        am = [sh['angular_momentum'] for sh in eldata['electron_shells']]

        new_pattern = []
        for sh in eldata['electron_shells']:
            new_pattern.append('{}{}'.format(len(sh['coefficients']), lut.amint_to_char(sh['angular_momentum'])))

        print(lut.element_sym_from_Z(el, True), ''.join(new_pattern))
        assert new_pattern == el_split
    print()
