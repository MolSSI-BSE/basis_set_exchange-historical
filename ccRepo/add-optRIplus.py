#!/usr/bin/env python3

from basis_set_exchange import curate

for b in ['cc-pVDZ-F12_OPTRIplus', 'cc-pVTZ-F12_OPTRIplus', 'cc-pVQZ-F12_OPTRIplus']:
    curate.add_basis(bs_file='parsed/{}.gbasis'.format(b),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='dunning_fit',
                     file_base=b,
                     name=b.replace('plus','+'),
                     family='dunning_fit',
                     role='optri',
                     description=b.replace('plus','+'),
                     version=1,
                     revision_description="Data from Grant Hill's ccRepo",
                     data_source="Data from Grant Hill's ccRepo",
                     refs=['shaw2017a']
                     )
