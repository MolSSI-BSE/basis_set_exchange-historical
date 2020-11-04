#!/usr/bin/env python3

from basis_set_exchange import curate
print(curate)

flist = {
'aug-pcH-1': 'aug-pcH-1',
'aug-pcH-2': 'aug-pcH-2',
'aug-pcH-3': 'aug-pcH-3',
'aug-pcH-4': 'aug-pcH-4',
'pcH-1':     'pcH-1',
'pcH-2':     'pcH-2',
'pcH-3':     'pcH-3',
'pcH-4':     'pcH-4',
}


for k, v in flist.items():
    curate.add_basis(bs_file=k,
                     data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     subdir='jensen',
                     file_base=k,
                     name=k,
                     family='jensen',
                     role='orbital',
                     description=v,
                     version='1',
                     revision_description='Data from Frank Jensen',
                     data_source='Data from Frank Jensen',
                     refs='jakobsen2019a',
                     file_fmt='dalton'
    )
