#!/usr/bin/env python3

from basis_set_exchange import curate

for v in ['S', 'D', 'T']:
    basis='s{}ZHF'.format(v)
    curate.add_basis(bs_file='{}.gbs.bz2'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='sigmaNZ',
                     file_base=basis,
                     name=basis,
                     family='sigmaNZ',
                     role='orbital',
                     description='{} basis for Hellmann-Feynman forces',
                     version=1,
                     revision_description='Data from Susi Lehtola',
                     data_source='Data from Susi Lehtola',
                     refs='pathak2022a',
                     file_fmt=None
                     )
