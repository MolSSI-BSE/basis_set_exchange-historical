#!/usr/bin/env python3

import requests
import time

url="http://tyr0.chem.wsu.edu/~kipeters/basissets/basisform-v5zf12.php"

for basis in ['cc-pVDZ-F12rev2', 'cc-pVTZ-F12rev2', 'cc-pVQZ-F12rev2', 'cc-pV5Z-F12rev2']: 
    print('Basis ' + basis + '...', end='')
    data = {'basis': basis,
            'element': 'H',
            'program': 'NWChem'
           }
 
    r = requests.post(url, data=data)
    print("Retrieved")
    with  open('{}-H.html'.format(basis), 'w') as f:
        f.write(r.text)
    time.sleep(10)
