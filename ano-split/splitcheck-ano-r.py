#!/usr/bin/env python3

import re
import sys
import copy
from basis_set_exchange import api, fileio, lut



with open('splitmap.txt', 'r') as f:
    split_data = f.readlines()[2:]

split_data = [x.strip().split() for x in split_data]
split_data = {lut.element_Z_from_sym(x[0], as_str=True): (x[1], x[2], x[3], x[4]) for x in split_data}

names = ['ANO-R0', 'ANO-R1', 'ANO-R2', 'ANO-R3']
for idx,name in enumerate(names):
    print(name)
    new_basis = api.get_basis(name)
    for el,eldata in new_basis['elements'].items():
        el_split = split_data[el][idx]
        el_split = re.findall(r'\d+[a-z]+', el_split)

        am = [sh['angular_momentum'] for sh in eldata['electron_shells']]

        new_pattern = []
        for sh in eldata['electron_shells']:
            new_pattern.append('{}{}'.format(len(sh['coefficients']), lut.amint_to_char(sh['angular_momentum'])))

        print(lut.element_sym_from_Z(el, True), ''.join(new_pattern))
        assert new_pattern == el_split
    print()
