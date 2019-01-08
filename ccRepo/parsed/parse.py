#!/usr/bin/env python3

import sys

data = {}

for fpath in sys.argv[1:]:
    with open(fpath, 'r') as f:
        data_lines = f.readlines()

    cur_data = []
    cur_basis = None

    for x in data_lines:
        if ':' in x:
            s = x.split(':')

            if cur_basis is not None:
                if not cur_basis in data:
                    data[cur_basis] = []
                data[cur_basis].extend(cur_data)

            cur_basis = s[1]
            cur_data = [x]
        else:
            cur_data.append(x)

    if cur_basis is not None:
        if not cur_basis in data:
            data[cur_basis] = []
        data[cur_basis].extend(cur_data)


for k,v in data.items():
    with open(k + '.gbasis', 'w') as f:
        f.write(''.join(v))
