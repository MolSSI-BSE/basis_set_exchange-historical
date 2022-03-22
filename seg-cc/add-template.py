#!/usr/bin/env python3

from basis_set_exchange import curate

for aug in ["", "aug-"]:
    for cv in ["", "wC"]:
        for v in ['D', 'T', 'Q', '5']:
            basis='{}seg-cc-p{}V{}Z-PP'.format(aug, cv, v)
            print('Processing {}'.format(basis))
            curate.add_basis(bs_file='{}.nw'.format(basis.lower()),
                             data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                             subdir='dunning',
                             file_base=basis,
                             name=basis,
                             family='dunning',
                             role='orbital',
                             description=basis,
                             version=1,
                             revision_description='Data from George Schoendorff',
                             data_source='Data from George Schoendorff',
                             refs='schoendorff2022a',
                             file_fmt=None
                             )
