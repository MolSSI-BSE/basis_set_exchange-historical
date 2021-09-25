#!/usr/bin/env python3

from basis_set_exchange import curate

for basis in ['ano-r', 'ano-r0', 'ano-r1', 'ano-r2', 'ano-r3']:
    print('Parsing {}'.format(basis))
    curate.add_basis(bs_file='{}.2.molcas'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='ano',
                     file_base=basis.upper(),
                     name=basis.upper(),
                     family='ano',
                     role='orbital',
                     description=basis.upper(),
                     version='2',
                     revision_description='Data from supporting information of erratum',
                     data_source='Data from supporting information of erratum',
                     refs=['zobel2020a', 'zobel2021a'],
                     file_fmt=None
                     )
