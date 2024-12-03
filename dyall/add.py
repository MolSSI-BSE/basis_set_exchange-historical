#!/usr/bin/env python3

from basis_set_exchange import lut, manip, curate

flavors = {'v' : 'valence', 'cv' : 'core-valence', 'ae' : 'all-electron'}
augmentations = {'' : '', 'a' : 'augmented '}

def parse_file(f):
    data = f.readlines()
    # Remove comment lines
    data = [line for line in data if not line.startswith('$') and len(line.strip())>0]

    element_exponents = {}
    iline = 0
    while iline < len(data):
        if not data[iline].startswith('a '):
            print(f'Skipping {data[iline]}')
            iline += 1
        
        if data[iline].startswith('a '):
            # New entry, read Z
            Z = data[iline].split()[1]
            iline += 1
            # Exponents
            exponents = []
            while iline < len(data) and not data[iline].startswith('a '):
                entries = data[iline].split()
                if len(entries) != 3:
                    raise RuntimeError(f'Error on data line {data[iline]}')
                num_exps = int(entries[0])
                assert entries[1] == '0' and entries[2] == '0'
                iline += 1
                exps = []
                for iexp in range(num_exps):
                    exps.append(data[iline].strip())
                    iline += 1
                exponents.append(exps)
            element_exponents[Z] = exponents
    return element_exponents

def write_gaussian94(fname, element_exponents):
    out = open(fname, 'w')
    for element in element_exponents:
        out.write(f'{lut.element_sym_from_Z(element)} 0\n')
        for am, exponents in enumerate(element_exponents[element]):
            for exponent in exponents:
                out.write(f'L={am} 1 1.0\n{exponent} 1.0\n')
        out.write('****\n')
    out.close()

def form_references(zeta, flavor, augmentation):
    refs = {}
    blocks = lut.all_element_blocks()
    for Z in range(1,119):
        def add_ref(ref):
            if Z not in refs:
                refs[Z] = [ref]
            else:
                refs[Z].append(ref)

        if zeta == 2 and (blocks[Z] == '4p' or blocks[Z] == '5p' or blocks[Z] == '6p'):
            # K. G. Dyall, Theor. Chem. Acc. 99, 366 (1998). Relativistic and nonrelativistic finite nucleus optimized double zeta basis sets for the 4p, 5p and 6p elements.
            add_ref('dyall1998a')
        if zeta == 3 and (blocks[Z] == '4p' or blocks[Z] == '5p' or blocks[Z] == '6p'):
            # K. G. Dyall, Theor. Chem. Acc. 108, 335 (2002). Relativistic and nonrelativistic energy-optimized polarized triple-zeta basis sets for the 4p, 5p and 6p elements
            add_ref('dyall2002a')
        if blocks[Z] == '5d' and (zeta == 2 or zeta == 3 or zeta == 4):
            # K. G. Dyall, Theor. Chem. Acc. 112, 403 (2004). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 5d elements Hf - Hg.
            add_ref('dyall2004a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and (blocks[Z] == '4p' or blocks[Z] == '5p' or blocks[Z] == '6p'):
            # K. G. Dyall, Theor. Chem. Acc. 115, 441 (2006). Relativistic quadruple-zeta basis sets and revised triple-zeta and double-zeta basis sets for the 4p, 5p and 6p elements.
            add_ref('dyall2006a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and blocks[Z] == '4d':
            # K. G. Dyall, Theor. Chem. Acc. 117, 483 (2006). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 4d elements Y - Cd.
            add_ref('dyall2007a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and blocks[Z] == '5f':
            # K. G. Dyall, Theor. Chem. Acc. 117, 491 (2007). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the actinide elements Ac - Lr.
            add_ref('dyall2007b')
        if (zeta == 2 or zeta == 3 or zeta == 4) and (blocks[Z] == '4s' or blocks[Z] == '5s' or blocks[Z] == '6s'):
            # K. G. Dyall, J. Phys. Chem. A. 113, 12638 (2009). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 4s, 5s, 6s, and 7s elements
            add_ref('dyall2009a')
        if (zeta == 2 or zeta == 3) and blocks[Z] == '5d':
            # K. G. Dyall and A. S. P. Gomes, Theor. Chem. Acc. 125, 97 (2010). Revised relativistic basis sets for the 5d elements Hf - Hg
            add_ref('dyall2010a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and blocks[Z] == '4f':
            # A. S. P. Gomes, K. G. Dyall, and L. Visscher, Theor. Chem. Acc. 127, 369 (2010). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the lanthanide elements La - Lu
            add_ref('gomes2010a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and blocks[Z] == '6d':
            # K. G. Dyall, Theor. Chem. Acc. 129, 603 (2011). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 6d elements Rf - Cn.
            add_ref('dyall2011a')
        if (zeta == 2 or zeta == 3 or zeta == 4) and blocks[Z] == '7p':
            # K. G. Dyall, Theor. Chem. Acc. 131, 1172 (2012). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the 7p elements, with atomic and molecular applications
            add_ref('dyall2012a')

        if (zeta == 2 or zeta == 3 or zeta == 4) and ( Z >= 1 and Z <= 18):
            # K. G. Dyall, Theor. Chem. Acc. 135, 128 (2016). Relativistic double-zeta, triple-zeta, and quadruple-zeta basis sets for the light elements H - Ar
            add_ref('dyall2012a')

        # If there are no references yet, the set has to be unpublished
        if Z not in refs:
            add_ref('dyallXXXXa')

        if flavor == 'ae' or flavor == 'cv' and Z >= 31 and Z <= 118:
            # K. G. Dyall, Theor. Chem. Acc. 131, 1217 (2012). Core correlating basis functions for elements 31 - 118
            add_ref('dyall2012b')

        if augmentation == 'a' and (blocks[Z][1] == 's' or blocks[Z][1] == 'd'):
            # K. G. Dyall, P. Tecmer, and A. Sunaga, J. Chem. Theor. Comput. 19, 198 (2023). Diffuse basis functions for relativistic s and d block Gaussian basis sets
            add_ref('dyall2023a')

        # All sets come from Dyall's Zenodo
        add_ref('dyall2023b')
    return refs


for flavor in flavors:
    for augmentation in augmentations:
        for zeta in range(2,5):
            print(f'Running {flavor=} {augmentation=} {zeta=}')
            with open(f'dyall.{augmentation}{flavor}{zeta}z') as f:
                basis_name = f'dyall-{augmentation}{flavor}{zeta}z'
                print(f'Parsing file {basis_name}')
                basis_data = parse_file(f)
                write_gaussian94(f'{basis_name}.1.gbs', basis_data)
                print(f'Parsed {basis_name}')

                # Form the reference database
                all_refs = form_references(zeta, flavor, augmentation)
                # Only include references for elements that actually exist in basis set
                refs = {element : all_refs[int(element)] for element in basis_data}

                curate.add_basis(bs_file=f'{basis_name}.1.gbs',
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='dyall',
                 file_base=basis_name,
                 name=basis_name,
                 family='dyall',
                 role='orbital',
                 description=f'Dyall\'s {augmentations[augmentation]}{flavors[flavor]} {zeta}-zeta primitive basis set',
                 version=1,
                 revision_description='Data from https://zenodo.org/records/7574629',
                 data_source='Data from https://zenodo.org/records/7574629',
                 refs=refs,
                 file_fmt=None
                 )
