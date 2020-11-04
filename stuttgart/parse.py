#!/usr/bin/env python3

import os
import sys
import re
from pprint import pprint
import basis_set_exchange as bse
from basis_set_exchange import curate, validator
from collections import defaultdict

refmap = {
     "1": "fuentealba1982a",       "2": "szentpaly1982a",   "3": "fuentealba1983a",    "4": "stoll1984a",       "5": "fuentealba1985a",
     "6": "wedig1986a",            "7": "dolg1987a",        "8": "igelmann1988a",      "9": "dolg1989b",       "10": "schwerdtfeger1989a",
     "11": "dolg1989c",           "12": "andrae1990a",     "13": "kaupp1991a",        "14": "kuchle1991a",     "15": "dolg1991a",
     "16": "dolg1992a",           "17": "bergner1993a",    "18": "dolg1993c",         "19": "dolg1993a",       "20": "haussermann1993a",
     "21": "kuchle1994a",         "22": "nicklass1995a",   "23": "leininger1996a",    "24": "leininger1996b",  "25": "leininger1997a",
     "26": "schautz1998a",        "27": "wang1998a",       "28": "mourik2000a",       "29": "metz2000a",       "30": "martin2001a",
     "31": "cao2001a cao2002a",   "32": "stoll2002a",      "33": "cao2003a cao2004a", "34": "kuchleXXXXz",     "35": "peterson2003a",
     "36": "peterson2003b",       "37": "figgen2005a",     "38": "lim2005a",          "39": "peterson2005a",   "40": "yang2005a",
     "41": "lim2006a",            "42": "peterson2006a",   "43": "peterson2007a",     "44": "moritz2007a",     "45": "moritz2007b",
     "46": "moritz2008a",         "47": "pantazis2009a",   "48": "figgen2009a",       "49": "weigend2010a",    "50": "dolg2009a",
     "51": "hangele2012a",        "52": "hangele2013a",    "53": "hangele2013b",      "54": "weigand2014a",
     "a1": "poppeXXXXa",          "a2": "fuentealba1984a", "a3": "fuentealba1988a",   "a4": "igelmann1988a",   "a5": 'igelmann1987a',
     "a6": 'haussermann1988a',    "a7": "andrae1989a",     "a8": "kuchle1993a",       "a9": "bergner1990a",   "a10": "dolg1997a",
    "a11": 'schwerdtfeger1999a', "a12": 'cao2002b'
}

refmap = {x:v.split(' ') for x,v in refmap.items()}

# Map from their symbols to IUPAC
elmap = { 'ut': 'uut',
          'up': 'uup',
          'us': 'uus',
          'uo': 'uuo',
          'un': 'uue',
          'ux': 'ubn'
        }
         



def find_references(comment):
    # Sometimes listed explicitly
    # cao2002a = X. Cao, M. Dolg, J. Molec. Struct. Theochem 581 (2002) 139
    # dolg1989d = M.Dolg, Dissertation 1989
    # igelmann1987a = Igel-Mann Dissertation
    # PP. von D. Andrae = andraeXXXXa
    # von A. Bergner, 1990 = bergner1990b
    comment = comment.lower()

    refs = []

    m = re.findall(r'ref[\., ] *(a?[0-9]{1,3})', comment)
    for x in m:
        refs.extend(refmap[x])
    if 'theochem 581' in comment:
            refs.append('cao2002a')
    if 'dolg, dissertation' in comment:
            refs.append('dolg1989d')
    if 'mann, dissertation' in comment:
            refs.append('igelmann1987a')
    if 'von d. andrae' in comment:
            refs.append('andraeXXXXa')
    if 'von a. bergner, 1990' in comment:
            refs.append('bergner1990b')
        
    return set(refs)


def _parse_basis_block(block):
    am = bse.lut.amchar_to_int(block['am'])
    ft = 'gto' if am[0] < 2 else 'gto_spherical'
    new_shell = {'function_type': ft,
                 'region': '',
                 'angular_momentum': bse.lut.amchar_to_int(block['am'])
                }

    nprim = int(block['nprim'])
    numbers = block['numbers']

    # The first numbers are exponents
    # The rest are coefficients
    exponents = numbers[:nprim]
    ctmp = numbers[nprim:]

    last = 0

    # Now coefficients according to the contraction patterns
    coefficients = []
    for cp in block['cont_patterns']:
        start, end = cp.split('.')
        start = int(start)-1
        end = int(end)

        c = ['0.00000000']*nprim
        c[start:end] = ctmp[:end-start]
        coefficients.append(c)

        ctmp = ctmp[end-start:]
        last = end

    # Handle leftover (uncontracted) exponents
    for i in range(last, len(exponents)):
        c = ['0.00000000']*nprim
        c[i] = '1.00000000'
        coefficients.append(c)

    new_shell['exponents'] = exponents
    new_shell['coefficients'] = coefficients
    return new_shell


def _parse_ecp_block(block):
    # Returns two lists of potentials - scalar and spinorbit

    lmax = int(block['lmax'])
    lmaxso = int(block['lmaxso'])
    numbers = block['numbers']

    # rows go from [0,lmax] for scalar,
    # and then [1,lmaxso] for spinorbit

    scalar_data = []
    for i in range(0, lmax+1):
        nentry = int(numbers.pop(0))
        new_pot = {'ecp_type': 'scalar_ecp',
                   'angular_momentum': [lmax if i == 0 else i-1],
                   'r_exponents': [],
                   'gaussian_exponents': [],
                   'coefficients': []
                  }
        
        for j in range(nentry):
            r = int(numbers.pop(0))
            gexponent = numbers.pop(0)
            coefficient = numbers.pop(0)
            new_pot['r_exponents'].append(r)
            new_pot['gaussian_exponents'].append(gexponent)
            new_pot['coefficients'].append(coefficient)

        new_pot['coefficients'] = [new_pot['coefficients']]
        scalar_data.append(new_pot)
    
    so_data = []
    for i in range(0, lmaxso):
        nentry = int(numbers.pop(0))
        new_pot = {'ecp_type': 'spinorbit_ecp',
                   'angular_momentum': [i+1],
                   'r_exponents': [],
                   'gaussian_exponents': [],
                   'coefficients': []
                  }
        
        for j in range(nentry):
            r = int(numbers.pop(0))
            gexponent = numbers.pop(0)
            coefficient = numbers.pop(0)
            new_pot['r_exponents'].append(r)
            new_pot['gaussian_exponents'].append(gexponent)
            new_pot['coefficients'].append(coefficient)

        new_pot['coefficients'] = [new_pot['coefficients']]
        so_data.append(new_pot)

    return scalar_data, so_data


def parse_block(idx):
    line = lines[idx]

    info = line.split()
    el = info[0]

    if el.lower() in elmap:
        el = elmap[el.lower()]
    el_z = str(bse.lut.element_Z_from_sym(el))
    block_type = info[1].lower()

    colon = info.index(':')
    names = ' '.join(info[2:colon])
    idx += 1
    comment = lines[idx]
    idx += 1

    if block_type == 'ecp':
        nelec, lmax, lmaxso, nparam = info[-4:]

        numbers = []
        line = lines[idx]
        while not line[0].isalpha():
            numbers.append(line)    
            idx += 1
            line = lines[idx]

        numbers = ' '.join(numbers)
        numbers = numbers.replace('D+', 'E+')
        numbers = numbers.replace('D-', 'E-')
        numbers = numbers.split()

        data = { 'lmax': lmax,
                 'lmaxso': lmaxso,
                 'numbers': numbers}

        parsed_data = _parse_ecp_block(data)
        parsed_data = (nelec, *parsed_data)
                 
        return (idx, 'ECP', comment, names, el_z, parsed_data)
    else:
        # Found a electron basis
        am = block_type

        nprim = info[colon+1]
        if len(info) > colon+2:
            ncont = info[colon+2]
            cont_patterns = info[colon+3:]
        else:
            ncont = 0
            cont_patterns = []

        numbers = []
        line = lines[idx]

        while not line[0].isalpha():
            numbers.append(line)    
            idx += 1
            line = lines[idx]

        numbers = ' '.join(numbers)
        numbers = numbers.replace('D+', 'E+')
        numbers = numbers.replace('D-', 'E-')
        numbers = numbers.split()

        data = { 'am': am,
                 'nprim': nprim,
                 'ncont': ncont,
                 'cont_patterns': cont_patterns,
                 'numbers': numbers }

        parsed_data = _parse_basis_block(data)

        return (idx, 'BASIS', comment, names, el_z, parsed_data)



#############################
# START PARSING THE FILE HERE
#############################
with open('LIBMOL.ecps', 'r') as fp:
    lines = [x.strip() for x in fp.readlines()]
lines = [x for x in lines if not x.startswith('*')]
lines = [x for x in lines if len(x) > 0]

idx = 0
ecp_data = defaultdict(lambda: defaultdict(list))
electron_data = defaultdict(lambda: defaultdict(list))

while idx < len(lines):
    idx, block_type, comment, names, el_z, data = parse_block(idx)

    if block_type == 'ECP':
        ecp_data[names][el_z].append({'comment': comment, 'data': data})
    else:
        electron_data[names][el_z].append({'comment': comment, 'data': data})

    if lines[idx] == 'ENDENDEND':
        break

#pprint(ecp_data)
#pprint(electron_data)

all_comp_files = []

# Create files for all the electron basis sets
for bsname,bsdata in electron_data.items():
    comp_file_path = '/tmp/bsetmp/' + bsname + '.1.json'
    comp_file = curate.create_skel('component')

    all_comments = set()
    for el, eldata in bsdata.items():
        comments = [x['comment'] for x in eldata]
        shells = [x['data'] for x in eldata]
        
        all_refs = set()
        for c in comments:
            all_comments.add(c)
            all_refs.update(find_references(c))

        # Add it to the appropriate place
        comp_file['elements'][el] = { 'electron_shells': shells,
                                      'references': list(all_refs) }

    comp_file['notes'] = '::'.join(all_comments)
    bse.fileio.write_json_basis(comp_file_path, comp_file)
    all_comp_files.append(comp_file_path)

# Create files for all the ecp sets

for bsname,bsdata in ecp_data.items():
    comp_file_path = '/tmp/bsetmp/' + bsname + '-ECP.1.json'
    comp_file = curate.create_skel('component')

    compso_file_path = '/tmp/bsetmp/' + bsname + '-SOECP.1.json'
    compso_file = curate.create_skel('component')

    all_comments = set()
    for el, eldata in bsdata.items():
        if len(eldata) != 1:
            raise RuntimeError("WTF")

        eldata = eldata[0]

        comment = eldata['comment']
        refs = find_references(comment)

        nelec, scalar_pots, so_pots = eldata['data']
        nelec = int(nelec)

        # Add it to the appropriate place
        comp_file['elements'][el] = { 'ecp_electrons': nelec,
                                      'ecp_potentials': scalar_pots,
                                      'references': list(refs)} 

        if len(so_pots) > 0:
            compso_file['elements'][el] = { 'ecp_electrons': nelec,
                                            'ecp_potentials': so_pots, 
                                            'references': list(refs)} 

    comp_file['notes'] = comment
    compso_file['notes'] = comment
    bse.fileio.write_json_basis(comp_file_path, comp_file)
    all_comp_files.append(comp_file_path)

    if len(compso_file['elements']) > 0:
        bse.fileio.write_json_basis(compso_file_path, compso_file)
        all_comp_files.append(compso_file_path)

print("Created " + str(len(all_comp_files)) + " files")


# Validate the created files
for fp in all_comp_files:
    print('Validating ' + fp)

    try:
        validator.validate_file('component', fp)
    except Exception as ex:
        print('    **** ' + str(ex))
