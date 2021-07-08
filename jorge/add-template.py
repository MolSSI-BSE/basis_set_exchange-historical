#!/usr/bin/env python3

from basis_set_exchange import curate

if False:
    curate.add_basis(bs_file='tzp-zora.gbs',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='jorge',
                     file_base='TZP-ZORA',
                     name='TZP-ZORA',
                     family='jorge',
                     role='orbital',
                     description='TZP-ZORA, all-electron triple-zeta basis for calculations with the ZORA approach',
                     version='1',
                     revision_description='Data from supporting information',
                     data_source='Data from supporting information',
                     refs='canalneto2021a',
                     file_fmt=None
                     )
curate.add_basis(bs_file='atzp-zora.gbs',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='jorge',
                 file_base='ATZP-ZORA',
                 name='ATZP-ZORA',
                 family='jorge',
                 role='orbital',
                 description='ATZP-ZORA, augmented all-electron triple-zeta basis for calculations with the ZORA approach',
                 version='1',
                 revision_description='Data from supporting information',
                 data_source='Data from supporting information',
                 refs='canalneto2021a',
                 file_fmt=None
                 )
