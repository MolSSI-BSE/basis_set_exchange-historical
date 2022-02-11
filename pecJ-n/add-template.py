#!/usr/bin/env python3

from basis_set_exchange import curate

for val in ['1', '2']:
    basis='pecJ-{}'.format(val)
    print('Parsing {}'.format(basis))
    curate.add_basis(bs_file='{}.1.cfour'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='pec',
                     file_base=basis,
                     name=basis,
                     family='pec',
                     role='orbital',
                     description=basis,
                     version='1',
                     revision_description='Data from supporting information',
                     data_source='Data from supporting information',
                     refs=['rusakov2021a'],
                     file_fmt='genbas'
                     )
