#!/usr/bin/env python3

import glob
import basis_set_exchange as bse
from basis_set_exchange import curate
import xml.etree.ElementTree as ET

def fix_number(n):
    return "{:.7f}".format(float(n))

dirlist = [
    "Sapporo-DKH3-DZP",
    "Sapporo-DKH3-DZP-diffuse",
    "Sapporo-DKH3-QZP",
    "Sapporo-DKH3-QZP-diffuse",
    "Sapporo-DKH3-TZP",
    "Sapporo-DKH3-TZP-diffuse",
    "Sapporo-DZP",
    "Sapporo-DZP-diffuse",
    "Sapporo-QZP",
    "Sapporo-QZP-diffuse",
    "Sapporo-TZP",
    "Sapporo-TZP-diffuse"
]

reflist = {
    "Bull. Univ. Electro. Comm., 5, 23 (1992)": "yamamoto1992a",
    "Theoret. Chem. Acc. 131, 1124 (2012)": "noro2012a",
    "Theoret. Chem. Acc. 132, (2013) 1363": "noro2013a",
    "Theoret. Chem. Acc. 131, 1247 (2012)": "sekiya2012a",
    "Theor. Chem. Acc., 109, 85-90 (2003)": "noro2003a",
    "Theor. Chem. Acc. 96, 243 (1997)": "tatewaki1997a",
    "Theor. Chem. Acc., 98, 25-32 (1997)": "noro1997a",
    "Theor. Chem. Acc. 102, 105 (1999)": "koga1999a",
    "Theor. Chem. Acc., 104, 146-152 (2000)": "noro2000a",
    "Theor. Chem. Acc., 106, 297-300 (2001)": "sekiya2001a",
    "Theor. Chem. Acc. 108, 41 (2002)": "koga2002a",
    "Theor. Chem. Acc., 121, 289-295 (2008)": "noro2008a",
    "Chem. Phys. Letters 481, 229-233 (2009)": "noro2009a",
    "J. Chem. Chem. 104, 8493 (1996)": "tatewaki1996a",
    "J. Mol. Struct.(Theochem), 451, 51-60 (1998)": "sekiya1998a",
    "Mol. Phys., 101, 65-71 (2003)": "osanai2003a",
    "unpublished": "moriyamaXXXXa"
}

for d in dirlist:
    filelist = glob.glob(d + '/xml/*.xml')

    component_json = curate.create_skel('component')
    component_json['description'] = d
    component_json['data_source'] = "Data from T. Noro"

    for f in filelist:
        bs_el_refs = []
        root = ET.parse(f).getroot()
        info = root.find('information')

        element = str(bse.lut.element_Z_from_sym(info.attrib['symbol_element']))

        if element in component_json['elements']:
            raise RuntimeError('wtf')


        refs = info.findall('reference')
        for ref in refs:
            ref_journal = ref.find('journal').text
            bs_el_refs.append(reflist[ref_journal])

        el_data = { 'references': bs_el_refs,
                    'electron_shells': [] } 

        body = root.find("body")
        for shell in body.findall("basis"):
            am = [int(shell.attrib['l'])]

            exponents = []
            coefficients = []
            for p in shell.findall('primitive'):
                exponents.append(fix_number(p.attrib['zeta']))
                coefficients.append(fix_number(p.attrib['coef']))

            if max(am) <= 1:
                func_type = 'gto'
            else:
                func_type = 'gto_spherical'

            new_shell = { 'function_type': func_type,
                          'region': '',
                          'angular_momentum': am,
                          'exponents': exponents,
                          'coefficients': [coefficients]
                        }
            el_data['electron_shells'].append(new_shell)

        component_json['elements'][element] = el_data


    element_json = curate.create_skel('element')
    table_json = curate.create_skel('table')
    md_json = curate.create_skel('metadata')

    element_json['elements'] = {k: {'components': [d + '.1.json']} for k in component_json['elements'].keys()}
    element_json['name'] = d
    element_json['description'] = d

    table_json['elements'] = {k:d + '.1.element.json' for k in component_json['elements'].keys()}
    table_json['revision_date'] = "2019-07-15"
    table_json['revision_description'] = "Data from T. Noro"

    md_json['family'] = 'sapporo'
    md_json['names'] = [d]
    md_json['role'] = 'orbital'

    bse.fileio.write_json_basis(d + '.1.json', component_json)    
    bse.fileio.write_json_basis(d + '.1.element.json', element_json)    
    bse.fileio.write_json_basis(d + '.1.table.json', table_json)    
    bse.fileio.write_json_basis(d + '.metadata.json', md_json)    
