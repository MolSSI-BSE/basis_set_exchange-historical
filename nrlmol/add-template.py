#!/usr/bin/env python3

from basis_set_exchange import curate, skel
from nrlmol import read_nrlmol

# Both DFO and DFO+ are in the same file; DFO+ just has some extra functions
dfo_data = open('DFO_ISYMGEN.nrlmol','r')
bs_lines = dfo_data.readlines()
dfo_els = read_nrlmol(bs_lines, extra=False)
dfop_els = read_nrlmol(bs_lines, extra=True)

dfo_data = skel.create_skel('component')
dfo_data['elements'] = dfo_els
dfop_data = skel.create_skel('component')
dfop_data['elements'] = dfop_els

curate.add_basis_from_dict(dfo_data,
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='dfo',
                 file_base='DFO-NRLMOL',
                 name='DFO-NRLMOL',
                 family='dfo',
                 role='orbital',
                 description='DFO basis from NRLMOL',
                 version=1,
                 revision_description='Data from NRLMOL',
                 data_source='Data from NRLMOL',
                 refs='porezag1999a'
                 )
curate.add_basis_from_dict(dfop_data,
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='dfo',
                 file_base='DFO+-NRLMOL',
                 name='DFO+-NRLMOL',
                 family='dfo',
                 role='orbital',
                 description='DFO+ basis from NRLMOL',
                 version=1,
                 revision_description='Data from NRLMOL',
                 data_source='Data from NRLMOL',
                 refs='porezag1999a'
                 )
