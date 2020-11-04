#!/usr/bin/env python3

from basis_set_exchange import curate

for basis in ['cc-pVDZ-F12rev2', 'cc-pVTZ-F12rev2', 'cc-pVQZ-F12rev2', 'cc-pV5Z-F12rev2']: 
    print(basis)
    curate.add_basis(bs_file=basis + '.nw.bz2',
                     data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     subdir='dunning_f12',
                     file_base=basis,
                     name=basis,
                     family='dunning_f12',
                     role='orbital',
                     description=basis,
                     version='1',
                     revision_description='Data from K. Peterson',
                     data_source='K. Peterson Website',
                     refs='peterson2015a',
                     file_fmt=None
    )
