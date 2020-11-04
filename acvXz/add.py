#!/usr/bin/env python3

from basis_set_exchange import curate

for x in [2, 3, 4]:
    curate.add_basis('acv{}z-J.c4bas.bz2'.format(x),
                     '/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     'acvXz-J',
                     'acv{}z-J'.format(x),
                     'acv{}z-J'.format(x),
                     'acvXz-J',
                     'orbital',
                     'acv{}z-J basis for indirect nuclear spin-spin coupling'.format(x),
                     '1',
                     'Data from Supplemental Information of publications',
                     'Data from Supplemental Information of publications',
                     'rusakov2019a'
    )
