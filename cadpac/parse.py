import re
from basis_set_exchange.readers.helpers import partition_lines, prune_lines, parse_line_regex
from basis_set_exchange.lut import element_sym_from_Z

# Read in data
with open('libfil.dat') as f:
    data = f.readlines()

# Identify basis blocks: string + nuclear charge
element_re = re.compile(r'^\s*([A-Za-z]+.*)\s+(\d+)\s*$')
# Note lines
note_re = re.compile(r'^NOTE ')
# Terminator
terminator_re = re.compile(r'^\s*\*\*\*\*\*\s*$')

# Shell enetry
shell_re = re.compile(r'^\s*(\d+)\s+([A-Za-z]+)\s+(\d+)\s*$')

# Collect the basis sets by name in a dictionary
basis_sets = {}
element_sections = partition_lines(data, element_re.match)
for iel, el in enumerate(element_sections):
    print('block {}'.format(iel))
    print(el)

    # Ensure this is a basis block
    if not element_re.match(el[0]):
        print('Skipping block {}'.format(iel))
        continue
    # Drop any notes
    el = [line for line in el if not note_re.match(line) and len(line.strip())>0]
    # Check termination
    if el[-1].strip() != '*****':
        raise RuntimeError('Incorrect terminator: {}'.format(el[-1].strip()))
    # Remove last line
    el.pop()

    # Check that there is no extra terminator
    nterm = sum([1 if terminator_re.match(line) else 0 for line in el])
    if nterm != 0:
        for iline, line in enumerate(el):
            if terminator_re.match(line):
                raise RuntimeError('Problem in entry: {}'.format(el[iline+1]))

    # Extract the name of the basis set
    elname, Z = parse_line_regex(element_re, el[0], 'elementbasisname, Z')

    # Clean out the basis set name from the string
    sym = element_sym_from_Z(Z).upper()
    assert elname[:len(sym)] == sym
    basname = elname[len(sym):].strip()

    print('basis = {} sym = {}'.format(basname, sym))

    # Parse the shells
    shell_sections = partition_lines(el[1:], shell_re.match)

    # Basis set in Gaussian'94 format
    elstr = '{} 0\n'.format(element_sym_from_Z(Z, normalize=True))
    for shell in shell_sections:
        # First line is just shell definition
        elstr += ' '.join(shell[0].split()[1:]) + ' 1.00\n'
        for line in shell[1:]:
            elstr += '    ' + '    '.join(line.split()[1:]) + '\n'
    elstr += '****\n'

    if basname not in basis_sets:
        basis_sets[basname] = []
    basis_sets[basname].append((Z, elstr))

# Sort the basis sets by element
for basname in basis_sets:
    basis_sets[basname] = sorted(basis_sets[basname], key=lambda x: x[0])

# Write out the basis sets
for basname in basis_sets:
    # Sort the basis sets by

    print('writing {}'.format(basname))
    fout=open('{}.gbs'.format(basname), 'w')

    basis = [x[1] for x in basis_sets[basname]]
    fout.write(''.join(basis))
    fout.close()
