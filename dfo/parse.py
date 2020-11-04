# This is a very, very quick & dirty script to convert the NRMOL output
# to gaussian

import re
import basis_set_exchange as bse
from basis_set_exchange import curate

def process_block(s):
    s = ' '.join(s)
    if not s.startswith('exp'):
        raise RuntimeError("Does not begin with exp")
    r = re.split(r' *(exp|[spdf]) *', s)
    r = [ x for x in r if len(x) > 0]

    assert len(r) % 2 == 0
    assert r[0] == 'exp'

    exponents = r[1].split()

    shells = []
    for i in range(2, len(r),2):
        sh = {'angular_momentum': r[i], 'exponents': exponents, 'coefficients': [r[i+1].split()]}
        shells.append(sh)
        
    return shells
    

lines = [x.strip() for x in open('dftbas.dat', 'r').readlines()]

elmap = {}
curblock = []

for l in lines:
    if 'DFO' in l:
        if len(curblock) > 0:
            if curblock[0] in elmap:
                raise RuntimeError("Duplicate: " + curblock[0])
            elmap[curblock[0]] = curblock[1:]
        curblock = []
    curblock.append(l)


if len(curblock) > 0:
    if curblock[0] in elmap:
        raise RuntimeError("Duplicate: " + curblock[0])
    elmap[curblock[0]] = curblock[1:]


elmap = {k: process_block(v) for k,v in elmap.items()}

from pprint import pprint

for basis in ['DFO-1', 'DFO-2', 'DFO-3']:
    s = ''
    for k,v in elmap.items():
        if basis in k:
            el = k.split()[0]
            s += el + '  0\n'
            for sh in v:
                nprim = len(sh['exponents'])
                s += sh['angular_momentum'].upper() + '   ' + str(nprim) +  '  1.000000\n'
                for i in range(nprim):
                    s += sh['exponents'][i] + '    ' + sh['coefficients'][0][i] + '\n'
            s += '****\n'

    with open(basis + '.gbs', 'w') as f:
        f.write(s)

