#!/usr/bin/env python3

from basis_set_exchange import curate

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
