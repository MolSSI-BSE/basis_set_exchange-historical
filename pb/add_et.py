#!/usr/bin/env python3

from basis_set_exchange import lut, manip, curate

def get_exponents(num_exps=8, max_am=2):
    # an even-tempered 8s8p8d basis set with exponents running from 2 sqrt(2) upwards
    a_min = 2.0**(1.5)
    shell_exponents = [a_min * (2)**(i/2) for i in range(num_exps)]
    print(shell_exponents)

    exponents = []
    for am in range(max_am+1):
        exponents.append(shell_exponents)
    return exponents

def form_gaussian94(exponents):
    # Form a Gaussian'94 string for the basis
    g94_str = 'H 0\n'
    for shell_am, shell_exps in enumerate(exponents):
        for expn in shell_exps:
            g94_str += f'L={shell_am} 1 1.0\n'
            g94_str += f' {expn:.14e} 1.0\n'
    g94_str += '****\n'
    return g94_str

def add_basis(num_exps, max_am, basis, ref, role):
    out = open(f'{basis}.gbs','w')
    exponents = get_exponents(num_exps=num_exps, max_am=max_am)
    out.write(form_gaussian94(exponents))
    out.close()

    curate.add_basis(bs_file='{}.gbs'.format(basis),
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='pb',
                 file_base=basis.lower(),
                 name=basis,
                 family='pb',
                 role=role,
                 description='Even-tempered 8s8p8d protonic basis',
                 version=1,
                 revision_description='Data from article',
                 data_source='Data from article',
                 refs=ref,
                 file_fmt=None
                 )

if False:
    add_basis(num_exps=8, max_am=2, basis='epc-8s8p8d', ref='yang2017a', role='orbital')

add_basis(num_exps=10, max_am=3, basis='epc-10s10p10d10f', ref='xu2022a', role='jkfit')
