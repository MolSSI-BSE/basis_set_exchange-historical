#!/usr/bin/env python3

from basis_set_exchange import curate

for basis in ['ANO-VT-DZ', 'ANO-VT-TZ','ANO-VT-QZ']:  
    curate.add_basis(bs_file='{}.txt.bz2'.format(basis),
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='ano_claudino',
                 file_base=basis,
                 name=basis,
                 family='ano_claudino',
                 role='orbital',
                 description=basis,
                 version=2,
                 revision_description='Data from github/danclaudino (ACES format); Gaussian\'94 format on the site is broken',
                 data_source='Data from D. Claudino',
                 refs={'claudino2016a', 'claudino2016b'},
                 file_fmt='genbas'
                 )
for basis in ['FANO-DZ', 'FANO-TZ','FANO-QZ', 'FANO-5Z', 'FANO-6Z']:  
    curate.add_basis(bs_file='{}.txt.bz2'.format(basis),
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='ano_claudino',
                 file_base=basis,
                 name=basis,
                 family='ano_claudino',
                 role='orbital',
                 description=basis,
                 version=2,
                 revision_description='Data from github/danclaudino (ACES format); Gaussian\'94 format on the site is broken',
                 data_source='Data from D. Claudino',
                 refs={'claudino2018a'},
                 file_fmt='genbas'
                 )
