#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='x2c-SVPall-s.tm.bz2',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='ahlrichs_x2c',
                 file_base='x2c-SVPall-s',
                 name='x2c-SVPall-s',
                 family='ahlrichs_x2c',
                 role='orbital',
                 description='All-electron relativistic split-valence for NMR shielding',
                 version='1',
                 revision_description='Data from Supporting info',
                 data_source='Supporting info of franzke2019a',
                 refs='franzke2019a',
                 file_fmt=None
)

curate.add_basis(bs_file='x2c-TZVPall-s.tm.bz2',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='ahlrichs_x2c',
                 file_base='x2c-TZVPall-s',
                 name='x2c-TZVPall-s',
                 family='ahlrichs_x2c',
                 role='orbital',
                 description='All-electron relativistic triple-zeta for NMR shielding',
                 version='1',
                 revision_description='Data from Supporting info',
                 data_source='Supporting info of franzke2019a',
                 refs='franzke2019a',
                 file_fmt=None
)


curate.add_basis(bs_file='x2c-TZVPPall-s.tm.bz2',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='ahlrichs_x2c',
                 file_base='x2c-TZVPPall-s',
                 name='x2c-TZVPPall-s',
                 family='ahlrichs_x2c',
                 role='orbital',
                 description='All-electron relativistic triple-zeta for NMR shielding',
                 version='1',
                 revision_description='Data from Supporting info',
                 data_source='Supporting info of franzke2019a',
                 refs='franzke2019a',
                 file_fmt=None
)
