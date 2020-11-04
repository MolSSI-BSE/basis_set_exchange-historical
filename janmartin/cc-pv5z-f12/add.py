#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='combined.nw',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='dunning_f12',
                 file_base='cc-pV5Z-F12',
                 name='cc-pV5Z-F12',
                 family='dunning_f12',
                 role='orbital',
                 description='cc-pV5Z-F12',
                 version='1',
                 revision_description='Data from K. Peterson',
                 data_source='K. Peterson Website',
                 refs='peterson2015a',
                 file_fmt=None
)
