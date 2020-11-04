#!/usr/bin/env python3

from basis_set_exchange import curate

if False:
    curate.add_basis(bs_file='pob-TZVP.crystal.bz2',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='pob',
                     file_base='pob-TZVP',
                     name='pob-TZVP',
                     family='pob',
                     role='orbital',
                     description='pob-TZVP',
                     version=1,
                     revision_description='Data from Bredow\'s web site',
                     data_source='Data from Bredow\'s web site',
                     refs='Peintinger2013a',
                     file_fmt=None
                     )

    for basis in ['pob-DZVP-rev2', 'pob-TZVP-rev2']:
        print('Adding {}'.format(basis))
        curate.add_basis(bs_file='{}.crystal.bz2'.format(basis),
                         data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                         subdir='pob',
                         file_base=basis,
                         name=basis,
                         family='pob',
                         role='orbital',
                         description=basis,
                         version=1,
                         revision_description='Data from Bredow\'s web site',
                         data_source='Data from Bredow\'s web site',
                         refs='Oliveira2019b',
                         file_fmt=None
                        )
