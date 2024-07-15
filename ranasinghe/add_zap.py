#!/usr/bin/env python3

from basis_set_exchange import curate

for n in range(2,7):
    name = str(n) + 'ZaP'
    print("Adding ", name)
    curate.add_basis(name.lower() + '.1.gbs.bz2',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='ranasinghe',
                     file_base=name.lower(),
                     name=name,
                     family='ranasinghe',
                     role='orbital',
                     description=f'{n}ZaP basis set of Zhong, Barnes, and Petersson',
                     version='1',
                     revision_description='Data from Supplementary Material',
                     data_source='Data from Supplementary Material',
                     refs='zhong2008a',
                     file_fmt=None
    )
