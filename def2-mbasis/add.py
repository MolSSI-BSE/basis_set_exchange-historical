#!/usr/bin/env python3

from basis_set_exchange import curate

bases = { 'def2-mTZVP' : ('grimme2018a','B97-3c'), 'def2-mTZVPP' : ('brandenburg2018a','r2SCAN-3c') }

for basis in bases:
    curate.add_basis(bs_file='{}.basis.txt'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='ahlrichs',
                     file_base=basis.lower(),
                     name=basis,
                     family='ahlrichs',
                     role='orbital',
                     description='{} basis for {} method'.format(basis,bases[basis][1]),
                     version=1,
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs=bases[basis][0],
                     file_fmt='turbomole'
                     )
    curate.add_basis(bs_file='{}.basis.txt'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='ahlrichs',
                     file_base='{}-RIJ'.format(basis).lower(),
                     name='{}-RIJ'.format(basis),
                     family='ahlrichs',
                     role='jfit',
                     description='{} RI-J basis for {} method'.format(basis,bases[basis][1]),
                     version=1,
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs=bases[basis][0],
                     file_fmt='turbomole'
                     )
