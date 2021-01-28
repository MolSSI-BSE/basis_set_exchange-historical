import basis_set_exchange
from basis_set_exchange.readers import helpers
from basis_set_exchange import curate
from basis_set_exchange import skel
import re
import os

# Element block
element_re = re.compile(r'-----------------------------------------------------------------')

def _parse_basis(basis_lines, bs_data):
    '''Parses an element block'''

    # Find charge
    iline = 0
    while iline < len(basis_lines):
        line = basis_lines[iline].strip()
        if line.startswith('CHARGE'):
            entries = basis_lines[iline].split()
            charge = entries[-1].replace('=','')
            element_Z = int(round(float(charge)))
            break
        iline += 1
    else:
        raise RuntimeError('Did not find CHARGE block')    
            
    # Find number of basis functions
    nprims = []
    while iline < len(basis_lines):
        line = basis_lines[iline].strip()
        if line.startswith('NUMBER OF BASIS FUNCTIONS'):
            entries = basis_lines[iline].split()
            nprims = [int(x) for x in entries[4:]]
            break
        iline += 1
    else:
        raise RuntimeError('Did not find NUMBER OF BASIS FUNCTIONS block')

    # Find orbital energies and coefficients
    while iline < len(basis_lines):
        line = basis_lines[iline].strip()
        if line.startswith('ORBITAL ENERGIES AND EXPANSION COEFFICIENTS'):
            break
        iline += 1
    else:
        raise RuntimeError('Did not find orbital coefficients block')

    iline += 1

    # Read in the exponents and contraction coefficients
    ncontr = []
    exps = []
    coeffs = []
    am = -1
    while True:
        line = basis_lines[iline].strip()
        # Ran out of the orbital block
        if len(line) == 0:
            break

        # Read in the orbital angular momentum
        orb_ams = line.split()
        iline += 1

        # It should be the same for all orbitals
        assert(all([x[-1] == orb_ams[0][-1] for x in orb_ams[1:]]))

        # Check against internal count
        am += 1
        assert(orb_ams[0][-1] == basis_set_exchange.lut.amint_to_char([am]).upper())
        
        # Number of orbitals is
        norb = len(orb_ams)-1
        ncontr.append(norb)

        # Next line is orbital energies; skip it
        assert(basis_lines[iline].strip().startswith('BASIS/ORB.ENERGY'))
        iline += 1

        # Now, read in the exponents and orbital coefficients
        am_exps = []
        am_coeffs = []
        for iprim in range(nprims[am]):
            values = basis_lines[iline].split()
            assert(len(values) == norb+2)
            am_exps.append(values[1])
            am_coeffs.append(values[2:])
            iline += 1
        exps.append(am_exps)
        coeffs.append(am_coeffs)

    assert am == len(exps)-1
    # Sanity check: check we can fit all electrons into the shells
    capacity = 0
    for shell_am in range(len(exps)):
        capacity += 2*(2*shell_am+1)*len(coeffs[shell_am][0])
    assert capacity >= element_Z

    str = 'Z = {}, capacity {}: '.format(element_Z, capacity)
    for shell_am in range(len(exps)):
        str += '{}{}'.format(len(exps[shell_am]), basis_set_exchange.lut.amint_to_char([shell_am]).upper())
    str += ' / '
    for shell_am in range(len(exps)):
        str += '{}{}'.format(len(coeffs[shell_am][0]), basis_set_exchange.lut.amint_to_char([shell_am]).upper())
    print(str)

    # Store the data
    element_data = helpers.create_element_data(bs_data, element_Z, 'electron_shells')
    for shell_am in range(len(exps)):
        func_type = 'gto' if shell_am < 2 else 'gto_spherical'
        shell = {
            'function_type': func_type,
            'region': '',
            'angular_momentum': [shell_am],
            'exponents': exps[shell_am],
            'coefficients': coeffs[shell_am]
        }
        element_data['electron_shells'].append(shell)
        
def parse(bs_data, fname):
    '''Parses the file'''

    print('Parsing {}'.format(fname))
    
    basis_lines = None
    with open(fname,'r') as filein:
        basis_lines = filein.readlines()

    element_sections = helpers.partition_lines(basis_lines, element_re.match, min_size=0)

    for es in element_sections:
        if len(es) < 3:
            continue
        _parse_basis(es, bs_data)


# Basis set dictionary
bs_data = {}
for filename in os.listdir('nonrel'):
    parse(bs_data, os.path.join('nonrel',filename))

# Ensure all basis sets have been parsed properly
for Z in range(1,104):
    if Z not in bs_data:
        raise RuntimeError('Z={} missing in the basis!\n'.format(Z))
print('All elements parsed')
    
koga_data = skel.create_skel('component')
koga_data['elements'] = bs_data
    
curate.add_basis_from_dict(koga_data,
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='koga',
                 file_base='Koga_atomic',
                 name='Koga unpolarized',
                 family='koga',
                 role='orbital',
                 description='Non-relativistic unpolarized basis sets for atomic calculations, designed for use in uncontracted form',
                 version=1,
                 revision_description='Data from Tatewaki\'s website',
                 data_source='Data from Tatewaki\'s website',
                 refs='koga2000a'
                 )
