#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='SBO4-DZ(d)-3G.gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='zorilla',
                 file_base='SBO4-DZ(d)-3G',
                 name='SBO4-DZ(d)-3G',
                 family='zorilla',
                 role='orbital',
                 description='SBO4-DZ(d)-3G Double-zeta expansion of simplified box orbitals',
                 version='1',
                 revision_description='Data from D. Zorilla',
                 data_source='Data from D. Zorilla',
                 refs='zorilla2019a',
                 file_fmt=None
)


curate.add_basis(bs_file='SBO4-SZ-3G.gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='zorilla',
                 file_base='SBO4-SZ-3G',
                 name='SBO4-SZ-3G',
                 family='zorilla',
                 role='orbital',
                 description='SBO4-SZ-3G Single-zeta expansion of simplified box orbitals',
                 version='1',
                 revision_description='Data from D. Zorilla',
                 data_source='Data from D. Zorilla',
                 refs='zorilla2018a',
                 file_fmt=None
)
