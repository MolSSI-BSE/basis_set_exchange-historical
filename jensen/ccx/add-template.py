#!/usr/bin/env python3

from basis_set_exchange import curate

valence='DTQ5'

for aug in [False, True]:
#   for nval in range(2,6):
    for nval in range(5,6):
        # Input file name
        infile='ccX{:02d}'.format(nval-1)
        # Basis set name is
        basname='ccX-{}Z'.format(valence[nval-2])
        if aug:
            infile = 'a'+infile
            basname = 'aug-'+basname
        # Description
        description='{} set for calculation of core excitations by the correlated wave function linear response and equation-of-motion methods'.format('Augmented basis' if aug else 'Basis')

        print('Parsing {} -> {}'.format(infile, basname))
        
        curate.add_basis(bs_file=infile,
                         data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                         subdir='jensen',
                         file_base=basname,
                         name=basname,
                         family='jensen',
                         role='orbital',
                         description=description,
                         version='1',
                         revision_description='Data from Frank Jensen',
                         data_source='Data directly from Frank Jensen',
                         refs='ambroise2021a',
                         file_fmt='gaussian94'
                        )
