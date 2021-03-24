#!/usr/bin/env python3

import basis_set_exchange
from basis_set_exchange.curate import add_basis_from_dict

def parse_file(bs_data, filename, num_am_expn, function_type):
    '''Parses the file'''

    exponent_dict = {}

    fin = open(filename,'r')
    data = fin.readlines()

    split_data = [d.split() for d in data]
    num_entries =  [len(entry) for entry in split_data]
    assert all([nentries == num_entries[0] for nentries in num_entries])

    # Need to swap rows and columns since data is stored columnwise
    element_basis = [[] for _, _ in enumerate(split_data[0])]
    for i, _ in enumerate(split_data):
        for icol, _ in enumerate(split_data[0]):
            element_basis[icol].append(split_data[i][icol])

    # Data is stored columnwise
    for eldata in element_basis:
        print(eldata)        
        
        element = eldata[0]

        # Length should be this match
        assert len(eldata) == 1+sum(num_am_expn)

        # Create element data
        element_Z = basis_set_exchange.lut.element_Z_from_sym(element)
        element_data = basis_set_exchange.readers.helpers.create_element_data(bs_data, str(element_Z), 'electron_shells')

        # Offset
        ioff = 1
        # Process angular momenta
        for am, nam in enumerate(num_am_expn):
            # Exponents
            exps = eldata[ioff:ioff+nam]
            ioff += nam

            # Loop over exponents
            for expn in exps:
                # Skip placeholders
                if expn.lower() == 'nan':
                    continue
                
                func_type = basis_set_exchange.readers.helpers.function_type_from_am([am], 'gto', function_type)
                shell = {
                    'function_type': func_type,
                    'region': '',
                    'angular_momentum': [am],
                    'exponents': [expn],
                    'coefficients': [['1.0']]
                }
                element_data['electron_shells'].append(shell)


#Paper states in results: the developed auxiliary basis functions are
#treated as Cartesian Gaussian functions for the 6-31G* basis set and
#spherical Gaussian functions for the 6-311G* basis set, according to
#the original definition.

# Table 1: 6s4p3d1f1g
t1_nam = [6, 4, 3, 1, 1]
# Table 1 continued: 7s5p4d2f1g
t1c_nam = [7, 5, 4, 2, 1]

# Process 6-31G**
b631gss_element_data = {}
parse_file(b631gss_element_data, 'table_s1.dat', t1_nam, 'cartesian')
parse_file(b631gss_element_data, 'table_s1_contd.dat', t1c_nam, 'cartesian')

# Table 2: 7s5p3d1f1g
t2_nam = [7, 5, 3, 1, 1]
# Table 2 continued: 8s6p4d2f1g
t2c_nam = [8, 6, 4, 2, 1]

b6311gss_element_data = {}
parse_file(b6311gss_element_data, 'table_s2.dat', t2_nam, 'spherical')
parse_file(b6311gss_element_data, 'table_s2_contd.dat', t2c_nam, 'spherical')

b631gss_rimp2_bs = basis_set_exchange.skel.create_skel('component')
b631gss_rimp2_bs['elements'] = b631gss_element_data

b6311gss_rimp2_bs = basis_set_exchange.skel.create_skel('component')
b6311gss_rimp2_bs['elements'] = b6311gss_element_data

add_basis_from_dict(b631gss_rimp2_bs,
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='pople',
                 file_base='6-31GSS-RIMP2',
                 name='6-31G**-RIMP2',
                 family='pople_fit',
                 role='rimp2',
                 description='RI-MP2 auxiliary basis for 6-31G** basis',
                 version=1,
                 revision_description="Data from supporting information",
                 data_source="Data from supporting information",
                 refs=['Tanaka2013a']
                 )
add_basis_from_dict(b6311gss_rimp2_bs,
                 data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                 subdir='pople',
                 file_base='6-311GSS-RIMP2',
                 name='6-311G**-RIMP2',
                 family='pople_fit',
                 role='rimp2',
                 description='RI-MP2 auxiliary basis for 6-311G** basis',
                 version=1,
                 revision_description="Data from supporting information",
                 data_source="Data from supporting information",
                 refs=['Tanaka2013a']
                 )
