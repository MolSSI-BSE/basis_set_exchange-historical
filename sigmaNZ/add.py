#!/usr/bin/env python3

from basis_set_exchange import curate

if False:
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

if True:
    for v in ['D', 'T', 'Q']:
        for aug in ['', 'a']:
            basis='{}sigma{}Z'.format(aug,v)
            curate.add_basis(bs_file='{}.1.mpro.bz2'.format(basis),
                         data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                         subdir='sigmaNZ',
                         file_base=basis,
                         name=basis,
                         family='sigmaNZ',
                         role='orbital',
                         description='{} basis',
                         version=1,
                         revision_description='Data from supporting information',
                         data_source='Data from supporting information',
                         refs='lopez2023a',
                         file_fmt=None
                         )
