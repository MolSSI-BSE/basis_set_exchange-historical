#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='dzvp-gga.d2k.bz2',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='demon2k',
                 file_base='deMon2k-DZVP-GGA',
                 name='deMon2k-DZVP-GGA',
                 family='demon2k',
                 role='orbital',
                 description='DZVP-GGA basis of the deMon2k code',
                 version='1',
                 revision_description='Data from deMon2k home page',
                 data_source='Direct from deMon2k home page',
                 refs='calaminici2007a',
                 file_fmt=None
)
