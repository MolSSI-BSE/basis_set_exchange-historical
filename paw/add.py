#!/usr/bin/env python3

from basis_set_exchange import curate
from basis import *

def collect_basis(basis):
    basis_string = 'BASIS "ao basis" SPHERICAL PRINT\n'
    for atom in dir(basis):
        # Skip class methods
        if atom.find('__') != -1:
            continue
        basis_string += f'#BASIS SET{getattr(basis, atom)}'
    basis_string += 'END\n'
    print(basis_string)
    print('\n\n')
    return basis_string

bases = {}
bases['PAW-L05'] = collect_basis(PAW_L0_5)
bases['PAW-L1'] = collect_basis(PAW_L1)
bases['PAW-L2'] = collect_basis(PAW_L1)
bases['PAW-L1-contracted'] = collect_basis(PAW_L1_contracted)
bases['PAW-L2-contracted'] = collect_basis(PAW_L1_contracted)

for basis in bases:
    # Write basis to file so it can be parsed
    out=open(f'{basis}.nw','w')
    out.write(bases[basis])
    out.close()
    # Parse
    curate.add_basis(bs_file=f'{basis}.nw',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='paw',
                 file_base=basis.lower(),
                 name=basis,
                 family='paw',
                 role='orbital',
                 description=f'{basis} basis set for use with PAW method',
                 version='1',
                 revision_description='Data from supporting information',
                 data_source='Data from supporting information',
                 refs='phung2020a',
                 file_fmt=None
                )
