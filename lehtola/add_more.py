#!/usr/bin/env python3

from basis_set_exchange import curate

polarization_type = ['without polarization', 'with 1 polarization shell', 'with 2 polarization shells', 'with 3 polarization shells']
polarization_name = ['', 'p1', 'p2', 'p3']
augmentation_type = ['', ', with more diffuse functions']
aug_name = ['', 'a']

for tol in [5, 7]:
    for pol in range(len(polarization_type)):
        for aug in [False, True]:
            name = '{}hgbs{}-{}'.format(aug_name[aug], polarization_name[pol], tol)
            basis_file = '{}.gbs'.format(name)
            description = 'Hydrogenic Gaussian basis set formed at tolerance 10^{{-{}}} {}{}'.format(tol, polarization_type[pol], augmentation_type[aug])
            print(f'{name=}')
            print(f'{basis_file=}')
            print(f'{description=}')
            curate.add_basis(bs_file=basis_file,
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='lehtola_hgbs',
                     file_base=name.upper(),
                     name=name.upper(),
                     family='lehtola_hgbs',
                     role='orbital',
                     description=description,
                     version=1,
                     revision_description='Data from S. Lehtola',
                     data_source='Direct from S. Lehtola',
                     refs='lehtola2020a',
                     file_fmt=None
    )
