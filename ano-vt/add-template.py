#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='ANO-VT-QZ.2.genbas.bz2',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='ano_claudino',
                 file_base='ANO-VT-QZ',
                 name='ANO-VT-QZ',
                 family='ano_claudino',
                 role='orbital',
                 description='ANO-VT-QZ (Atomic Natural Orbital - Virial Theorem - Quadruple Zeta)',
                 version=2,
                 revision_description='Retranslated from ACES format; original Gaussian\'94 data had negative exponents',
                 data_source='Data from D. Claudino',
                 refs=['claudino2016a', 'claudino2016b'],
                 file_fmt='genbas'
                 )
