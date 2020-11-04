#!/usr/bin/env python3

import glob
import basis_set_exchange as bse
from basis_set_exchange import curate
import xml.etree.ElementTree as ET

dirlist = [
    "Sapporo-DKH3-DZP-2012",
    "Sapporo-DKH3-DZP-2012-diffuse",
    "Sapporo-DKH3-QZP-2012",
    "Sapporo-DKH3-QZP-2012-diffuse",
    "Sapporo-DKH3-TZP-2012",
    "Sapporo-DKH3-TZP-2012-diffuse",
    "Sapporo-DZP-2012",
    "Sapporo-DZP-2012-diffuse",
    "Sapporo-QZP-2012",
    "Sapporo-QZP-2012-diffuse",
    "Sapporo-TZP-2012",
    "Sapporo-TZP-2012-diffuse"
]

journal_list = set()

for d in dirlist:
    filelist = glob.glob(d + '/xml/*.xml')

    for f in filelist:
        root = ET.parse(f).getroot()
        info = root.find('information')
        refs = info.findall('reference')
        for ref in refs:
            ref_journal = ref.find('journal').text
            journal_list.add(ref_journal)

for j in journal_list:
    print(j)
