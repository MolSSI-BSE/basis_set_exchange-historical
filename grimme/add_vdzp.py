#!/usr/bin/env python3

from basis_set_exchange import curate

curate.add_basis(bs_file='vDZP_TM.tm',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='grimme',
                 file_base='vdzp',
                 name='Grimme vDZP',
                 family='grimme',
                 role='orbital',
                 description='Small basis set used in wB97X-3c method',
                 version='1',
                 revision_description='Data from supporting information; re-added d-type ECP on F with vanishingly small coefficient to ensure basis is correctly parsed in all programs',
                 data_source='Data from supporting information; re-added d-type ECP on F with vanishingly small coefficient to ensure basis is correctly parsed in all programs',
                 refs='Mueller2023a',
                 file_fmt=None
                )
