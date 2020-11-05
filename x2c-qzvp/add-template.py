#!/usr/bin/env python3

from basis_set_exchange import curate

# Two components?
for twoc in [False, True]:
    # Number of polarization shells
    for npol in range(1,3):
        # For NMR shieldings?
        for nmr in [False, True]:
            # Basis set name is
            basname='x2c-QZVPall' if npol==1 else 'x2c-QZVPPall'
            # Description
            description='All-electron relativistic polarized quadruple-zeta basis' if npol==1 else 'All-electron relativistic doubly polarized quadruple-zeta basis'
            if twoc:
                basname+='-2c'
                description+=' for one-component calculations'
            else:
                description+=' for two-component calculations'

            if nmr:
                basname+='-s'
                description+=' of NMR shielding'

            curate.add_basis(bs_file='{}.tm.bz2'.format(basname),
                             data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                             subdir='ahlrichs_x2c',
                             file_base=basname,
                             name=basname,
                             family='ahlrichs_x2c',
                             role='orbital',
                             description=description,
                             version='1',
                             revision_description='Data from Supporting info',
                             data_source='Supporting info of franzke2020a',
                             refs='franzke2020a',
                             file_fmt=None
)

curate.add_basis(bs_file='x2c-JFIT.tm.bz2',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='ahlrichs_x2c',
                 file_base='x2c-JFIT',
                 name='x2c-JFIT',
                 family='ahlrichs_fit',
                 role='jfit',
                 description='Universal Coulomb fitting auxiliary basis for x2c basis sets',
                 version='1',
                 revision_description='Data from Supporting info',
                 data_source='Supporting info of franzke2019a',
                 refs='franzke2020a',
                 file_fmt=None
)
