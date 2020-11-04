#!/usr/bin/env python3

from basis_set_exchange import curate

#for n in range(2,6):
#    name = str(n) + 'ZaPa-NR-CV'
#
#    print("Adding ", name)
#    curate.add_basis(name.lower() + '.gbs.bz2',
#                     '/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
#                     'ranasinghe',
#                     name,
#                     name,
#                     'ranasinghe',
#                     'orbital',
#                     'Ranasinghe-Petersson 2ZaPa-NR-CV basis set',
#                     '1',
#                     'Data from Supplemental Information of publications',
#                     'Data from Supplemental Information of publications',
#                     'ranasinghe2015a'
#    )
#

for n in range(2,8):
    name = str(n) + 'ZaPa-NR'

    print("Adding ", name)
    curate.add_basis(name.lower() + '.gbs.bz2',
                     '/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     'ranasinghe',
                     name,
                     name,
                     'ranasinghe',
                     'orbital',
                     'Ranasinghe-Petersson 2ZaPa-NR basis set',
                     '1',
                     'Data from Supplemental Information of publications',
                     'Data from Supplemental Information of publications',
                     'ranasinghe2013a'
    )
