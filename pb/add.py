#!/usr/bin/env python3

from basis_set_exchange import lut, manip, curate

def parse_exponents(fname):
    data = open(fname,'r').readlines()
    # Clean up empty lines
    data = [line for line in data if len(line.split())>0]
    
    composition = [int(n) for n in data[0].split()]
    if len(data) != sum(composition)+1:
        raise ValueError(f'Invalid data in file {fname}')
    print(f'{fname=} {composition=}')

    shell_exponents = [[] for _ in composition]
    line_index = 1
    for angular_momentum in range(len(composition)):
        for nfunc in range(composition[angular_momentum]):
            shell_exponents[angular_momentum].append(data[line_index].strip())
            line_index += 1
    print(f'{fname=} {shell_exponents=}')
    return shell_exponents

def form_gaussian94(exponents):
    # Form a Gaussian'94 string for the basis
    g94_str = 'H 0\n'
    for shell_am, shell_exps in enumerate(exponents):
        for expn in shell_exps:
            g94_str += f'L={shell_am} 1 1.0\n'
            g94_str += f' {expn} 1.0\n'
    g94_str += '****\n'
    return g94_str

for basis in ['PB4-D', 'PB4-F1', 'PB4-F2', 'PB5-D', 'PB5-F', 'PB5-G', 'PB6-D', 'PB6-F', 'PB6-G', 'PB6-H']:
    exponents = parse_exponents(f'{basis.lower()}.dat')

    out = open(f'{basis}.gbs','w')
    out.write(form_gaussian94(exponents))
    out.close()

    curate.add_basis(bs_file='{}.gbs'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='pb',
                     file_base=basis.lower(),
                     name=basis,
                     family='pb',
                     role='orbital',
                     description=f'{basis} protonic basis',
                     version=1,
                     revision_description='Data from Table I',
                     data_source='Data from Table I',
                     refs='yu2020a',
                     file_fmt=None
                     )
