#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='6-311xxG(d,p).gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='zorilla',
                 file_base='6-311xxG(d,p)',
                 name='6-311xxG(d,p)',
                 family='zorilla',
                 role='orbital',
                 description='6-311xxG(d,p) basis set',
                 version='1',
                 revision_description='Data from D. Zorilla',
                 data_source='Data from D. Zorilla',
                 refs='sanchezmarquez2020a',
                 file_fmt=None
)
