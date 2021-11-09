#!/usr/bin/env python3

from basis_set_exchange import curate

for val in ['D', 'T', 'Q', '5']:
    for aug in ['', 'saug-', 'aug-']:
        basis='{}ano-pV{}Z'.format(aug, val)
        print('Parsing {}'.format(basis))
        curate.add_basis(bs_file='{}.bas'.format(basis),
                         data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                         subdir='ano',
                         file_base=basis.upper(),
                         name=basis.upper(),
                         family='ano',
                         role='orbital',
                         description=basis.upper(),
                         version='1',
                         revision_description='Data from supporting information',
                         data_source='Data from supporting information',
                         refs=['neese2011a'],
                         file_fmt='orca'
                         )
