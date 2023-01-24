#!/usr/bin/env python3

from basis_set_exchange import curate

if False:
    curate.add_basis(bs_file='minix.tm.bz2',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='grimme',
                     file_base='minix',
                     name='MINIX',
                     family='jensen',
                     role='orbital',
                     description='Small basis set used in HF-3c method',
                     version='1',
                     revision_description='Data from Stefan Grimme',
                     data_source='Data by email from Stefan Grimme',
                     refs='Sure2013a',
                     file_fmt=None
                 )
    curate.add_basis(bs_file='def2-mTZVP.tm',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='grimme',
                     file_base='def2-mTZVP',
                     name='def2-mTZVP',
                     family='grimme',
                     role='orbital',
                     description='Small basis set used in B97-3c method',
                     version='1',
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs='Brandenburg2018a',
                     file_fmt=None
                )
    curate.add_basis(bs_file='def2-mTZVP-jbas.tm',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='grimme',
                     file_base='def2-mTZVP-JFIT',
                     name='def2-mTZVP-JFIT',
                     family='grimme',
                     role='jfit',
                     description='Coulomb fitting set for B97-3c method',
                     version='1',
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs='Brandenburg2018a',
                     file_fmt=None
                )
if True:
    curate.add_basis(bs_file='def2-mTZVPP.tm',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='grimme',
                     file_base='def2-mTZVPP',
                     name='def2-mTZVPP',
                     family='grimme',
                     role='orbital',
                     description='Small basis set used in r2SCAN-3c method',
                     version='1',
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs='Grimme2021a',
                     file_fmt=None
                )
    curate.add_basis(bs_file='def2-mTZVPP-jbas.tm',
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='grimme',
                     file_base='def2-mTZVPP-JFIT',
                     name='def2-mTZVPP-JFIT',
                     family='grimme',
                     role='jfit',
                     description='Coulomb fitting set for r2SCAN-3c method',
                     version='1',
                     revision_description='Data from Sebastian Ehlert',
                     data_source='Data from Sebastian Ehlert',
                     refs='Grimme2021a',
                     file_fmt=None
                 )
