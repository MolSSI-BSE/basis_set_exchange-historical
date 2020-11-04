#!/usr/bin/env python3

from basis_set_exchange import curate

basis_list = [
'cc-pV5+dZ-X2C',
'cc-pV5Z-X2C',
'cc-pV6Z-X2C',
'cc-pVD+dZ-X2C',
'cc-pVDZ-X2C',
'cc-pVQ+dZ-X2C',
'cc-pVQZ-X2C',
'cc-pVT+dZ-X2C',
'cc-pVTZ-X2C'
]

for basis in basis_list:
    curate.add_basis(bs_file=basis + '.gbasis',
                     data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     subdir='dunning_x2c',
                     file_base='NEW_' + basis,
                     name='NEW_' + basis,
                     family='dunning_x2c',
                     role='orbital',
                     description=basis,
                     version=1,
                     revision_description='Data from ccRepo',
                     data_source='ccRepo/Grant Hill',
                     refs='peterson2018a',
                     file_fmt=None
    )
