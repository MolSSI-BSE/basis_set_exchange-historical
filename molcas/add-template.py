#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='ANO-R.molcas',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='ano',
                 file_base='ANO-R',
                 name='ANO-R',
                 family='ano',
                 role='orbital',
                 description='ANO-R',
                 version='1',
                 revision_description='Data from Supporting Information',
                 data_source='Data from Supporting Information',
                 refs='zobel2019a',
                 file_fmt=None
)
