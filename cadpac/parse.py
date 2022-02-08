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

    # Check that there is no extra terminator
    nterm = sum([1 if terminator_re.match(line) else 0 for line in el])
    if nterm != 1:
        for iline, line in enumerate(el):
            if terminator_re.match(line):
                raise RuntimeError('Problem in entry: {}'.format(el[iline+1]))
    
    # Extract the name of the basis set
    elname, Z = parse_line_regex(element_re, el[0], 'elementbasisname, Z')
    
    # Clean out the basis set name from the string
    sym = element_sym_from_Z(Z).upper()
    assert elname[:len(sym)] == sym
    basname = elname[len(sym):]

    print('basis = {} sym = {}'.format(basname, sym))
