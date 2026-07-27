#!/usr/bin/env python3

from basis_set_exchange import curate

refs={
    'pob-DZVP' : {'H-Br' : 'peintinger2013a', 'Rb-I' : 'laun2018a'},
    'pob-TZVP' : {'H-Br' : 'peintinger2013a', 'Rb-I' : 'laun2018a'},
    'pob-DZVP-rev2' : {'H-Br' : 'oliveira2019b'},
    'pob-TZVP-rev2' : {'H-Br' : 'oliveira2019b', 'Rb-I' : 'laun2022a', 'Cs-Ba,Hf-Po' : 'laun2021a', 'La-Lu' : 'seidler2023a'},
    # TBD: pob-DZVP-rev1 and pob-TZVP-rev1
}

versions={
    'pob-DZVP' : 1,
    'pob-TZVP' : 3,
    'pob-DZVP-rev2' : 2,
    'pob-TZVP-rev2' : 2,
}

for basis in refs:
    print('Adding {}'.format(basis))
    curate.add_basis(bs_file='{}.crystal.xz'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='pob',
                     file_base=basis,
                     name=basis,
                     family='pob',
                     role='orbital',
                     description=basis,
                     version=1,
                     revision_description='Data from Bredow',
                     data_source='Data from Bredow',
                     refs=refs[basis],
                     file_fmt=None
                     )
