#!/usr/bin/env python3

# Parses a basis set out of all the turbomole files

import os
import sys
import codecs
from basis_set_exchange import lut

all_basis = {}
basen_dir = sys.argv[1]
desired_basis = sys.argv[2]

for fname in os.listdir(basen_dir):
    fpath = os.path.join(basen_dir, fname)
    with codecs.open(fpath, 'r', "iso-8859-1") as f:
        lines = [x.strip() for x in f.readlines()]

    lines = [x for x in lines if len(x) > 0 and x[0] != '#']
    lines = lines[1:-1]

    n = 1
    while n < len(lines):
        while n < len(lines) and lines[n] == '*':
            n += 1
        if n >= len(lines):
            break

        if lines[n].startswith('$') and not lines[n].startswith('$ecp'):
            break

        if lines[n].startswith('$ecp'):
            n += 1

        while lines[n] == '*':
            n += 1

        all_bas_name = []
        while lines[n] != '*':
            el,bas_name = lines[n].split(maxsplit=1)
            bas_name = bas_name
            all_bas_name.append(bas_name)
            n += 1

        while lines[n] == '*':
            n += 1

        el_bas_data = {'links': [], 'shells': []}

        is_soecp = False
        while lines[n] != '*':
            if 'lsomax' in lines[n].lower():
                is_soecp = True
            elif lines[n].startswith('->'):
                el_bas_data['links'].append(lines[n][2:].strip())
            else:
                el_bas_data['shells'].append(lines[n])
            n += 1

        if is_soecp == True:
            n += 1
            while lines[n] != '*':
                if lines[n].startswith('->'):
                    el_bas_data['links'].append(lines[n][2:].strip())
                else:
                    el_bas_data['shells'].append(lines[n])
                n += 1
        
        for bn in all_bas_name:
            if not bn in all_basis:
                all_basis[bn] = {}
            if el in all_basis[bn] and all_basis[bn][el] != el_bas_data:
                print("basis {} already has element {}. Overwriting...".format(bn, el), file=sys.stderr)
            all_basis[bn][el] = el_bas_data



if not desired_basis in all_basis:
    raise RuntimeError("basis not found")

bas = all_basis[desired_basis]

for el,v in bas.items():
    while len(v['links']) > 0:
        linkstmp = v['links'].copy()
        v['links'] = []
        for l in linkstmp:
            el2,b2 = l.split(maxsplit=1)
            if el2 != el:   
                raise RuntimeError("bad link")
            ldata = all_basis[b2][el2]
            v['shells'].extend(ldata['shells'])
            v['links'].extend(ldata['links'])

allel = sorted(bas.keys(), key=lambda x:lut.element_Z_from_sym(x))

s = '*\n'
for el in allel:
    s += '{} {}\n*\n'.format(el, desired_basis)
    s += '\n'.join(bas[el]['shells'])
    s += '\n*\n'
print(s)

