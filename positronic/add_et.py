#!/usr/bin/env python3

from basis_set_exchange import lut, manip, curate

def get_exponents(num_exps, alpha, beta):
    # an even-tempered 8s8p8d basis set with exponents running from 2 sqrt(2) to 32
    shell_exponents = [alpha * (beta)**(i/(num_exps-1)) for i in range(num_exps)]
    print(shell_exponents)

    exponents = []
    for am in range(3):
        exponents.append(shell_exponents)
    return exponents

def form_gaussian94(exponents):
    # Form a Gaussian'94 string for the basis
    g94_str = 'H 0\n'
    for shell_am, shell_exps in enumerate(exponents):
        for expn in shell_exps:
            g94_str += f'L={shell_am} 1 1.0\n'
            g94_str += f' {expn} 1.0\n'
    g94_str += '****\n'
    return g94_str

basis_set_parameters = {
    'PsX-DZ' : [[5, 0.0190, 2.734], [3, 0.0591, 2.729], [2, 0.1165, 2.685]],
    'PsX-TZ' : [[6, 0.0171, 2.545], [4, 0.0496, 2.503], [3, 0.0951, 2.458], [2, 0.1596, 2.678]],
    'PsX-QZ' : [[7, 0.0160, 2.424], [5, 0.0417, 2.255], [4, 0.0813, 2.224], [3, 0.1177, 2.412], [2, 0.1419, 2.711]]
}

for basis in basis_set_parameters:
    exponents = get_exponents(*basis_set_parameters[basis])
    out = open(f'{basis}.gbs','w')
    out.write(form_gaussian94(exponents))
    out.close()

    curate.add_basis(bs_file='{}.gbs'.format(basis),
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='psx',
                     file_base=basis.lower(),
                     name=basis,
                     family='psx',
                     role='orbital',
                     description=f'Even-tempered {basis} positronic basis',
                     version=1,
                     revision_description='Data from supporting information',
                     data_source='Data from supporting information',
                     refs='moncada2020a',
                     file_fmt=None
                     )
