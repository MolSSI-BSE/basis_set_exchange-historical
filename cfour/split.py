#!/usr/bin/env python3

from pprint import pprint
import basis_set_exchange as bse

all_data = {}

def is_element(s):
    try:
        bse.lut.element_Z_from_sym(s)
    except Exception as e:
        return False
    return True

with open("GENBAS", 'r') as f:
    file_data = [x.strip() for x in f.readlines()]

curblock = []
for l in file_data:
    if not ':' in l:
        curblock.append(l)
    elif not is_element(l.split(':')[0]):
        curblock.append(l)
    else:
        if len(curblock) == 0:
            curblock = [l]
            continue

        bs_name = curblock[0].split(':', maxsplit=1)[1]
        if not bs_name in all_data:
            all_data[bs_name] = curblock
        else:
            all_data[bs_name].extend(curblock)
        curblock = [l]

if len(curblock) > 0:
    bs_name = curblock[0].split(':', maxsplit=1)[1]
    if not bs_name in all_data:
        all_data[bs_name] = curblock
    else:
        all_data[bs_name].extend(curblock)

for k, v in all_data.items():
    with open('split/' + k + '.genbas', 'w') as f:
        f.write('\n'.join(v))
