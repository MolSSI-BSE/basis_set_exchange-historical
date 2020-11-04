#!/usr/bin/env python3

import requests
import time

url="http://tyr0.chem.wsu.edu/~kipeters/basissets/basisform-v5zf12.php"

for element in ['H', 'He', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']:
    print('Element ' + element + '...', end='')
    data = {'basis': 'cc-pV5Z-F12',
            'element': element,
            'program': 'NWChem'
           }
 
    r = requests.post(url, data=data)
    print("Retrieved")
    with  open('cc-pV5Z-{}.html'.format(element), 'w') as f:
        f.write(r.text)
    time.sleep(10)
