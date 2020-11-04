#!/usr/bin/env python3


import sys
import os
from pprint import pprint
import basis_set_exchange as bse
from basis_set_exchange import curate
from collections import defaultdict

bs_data = {}
for f in os.listdir('/tmp/bsetmp'):
    p = os.path.join('/tmp/bsetmp', f)
    a = bse.fileio.read_json_basis(p)
    a = bse.manip.uncontract_general(a)
    bs_data[f] = a


for fp in sys.argv[1:]:
    print("File " + fp)
    to_find_orig = bse.fileio.read_json_basis(fp)
    to_find = bse.manip.uncontract_general(to_find_orig)

    found_map = defaultdict(list)

    for el,elv in to_find['elements'].items():
        found = False
        for fname,bsd in bs_data.items():
            if el not in bsd['elements']:
                continue

            if curate.compare_elements(elv, bsd['elements'][el], rel_tol=1e-8):
                if found:
                    print("****Found match: Element {} = {}".format(el, fname))
                else:
                    print("    Found match: Element {} = {}".format(el, fname))
                found = True

                to_find_orig['elements'][el]['references'] = bsd['elements'][el]['references']
                found_map[fname].append(el)

        if not found:
            print("    Element {} not found".format(el))

    print("  Summary for " + fp)
    for k,v in found_map.items():
        print("{} : {}".format(bse.misc.compact_elements(v), k))

    bse.fileio.write_json_basis(fp, to_find_orig) 
