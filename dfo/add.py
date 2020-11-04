#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='DFO-1.gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='dfo',
                 file_base='DFO-1',
                 name='DFO-1',
                 family='dfo',
                 role='orbital',
                 description='Optimized gaussian basis set for Density-functional calculations',
                 version='1',
                 revision_description='Data from SI of paper',
                 data_source='Data from SI of paper',
                 refs='porezag1999a',
                 file_fmt=None
)

curate.add_basis(bs_file='DFO-2.gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='dfo',
                 file_base='DFO-2',
                 name='DFO-2',
                 family='dfo',
                 role='orbital',
                 description='Optimized gaussian basis set for Density-functional calculations',
                 version='1',
                 revision_description='Data from SI of paper',
                 data_source='Data from SI of paper',
                 refs='porezag1999a',
                 file_fmt=None
)


curate.add_basis(bs_file='DFO-3.gbs',
                 data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                 subdir='dfo',
                 file_base='DFO-1-BHS',
                 name='DFO-1-BHS',
                 family='dfo',
                 role='orbital',
                 description='Optimized gaussian basis set for Density-functional calculations (requiring pseudopotential)',
                 version='1',
                 revision_description='Data from SI of paper',
                 data_source='Data from SI of paper',
                 refs='porezag1999a',
                 file_fmt=None
)

