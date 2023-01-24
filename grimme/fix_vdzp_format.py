import re
import basis_set_exchange


basis_in = open('basis_vDZP_TM.txt','r').readlines()
ecp_in = open('ecp_vDZP_TM.txt','r').readlines()

ret_basis = '$basis\n'

# Copy-paste orbital basis
iline = 0
while iline < len(basis_in):
    entries = basis_in[iline].split()
    while len(entries)==1 and entries[0]=='*':
        iline += 1
        if iline == len(basis_in):
            break
        entries = basis_in[iline].split()
    if iline == len(basis_in):
        break
    assert len(entries)==1
    # Get the element number
    Z=entries[0]

    # Create header
    ret_basis += '*\n{} vDZP\n*\n'.format(basis_set_exchange.lut.element_sym_from_Z(Z,normalize=True))
    # Copy data
    while True:
        iline += 1
        entries = basis_in[iline].split()
        if len(entries) != 2:
            break
        ret_basis += basis_in[iline]

# Copy-paste ECP
ret_basis += '*\n$ecp\n'
iline = 0
while iline < len(ecp_in):
    entries = ecp_in[iline].split()
    while len(entries)==1 and entries[0]=='*':
        iline += 1
        if iline == len(ecp_in):
            break
        entries = ecp_in[iline].split()
    if iline == len(ecp_in):
        break
    assert len(entries)==1
    # Get the element number
    Z=entries[0]

    # Create header
    ret_basis += '*\n{} vDZP-ecp\n*\n'.format(basis_set_exchange.lut.element_sym_from_Z(Z,normalize=True))
    # core and lmax
    iline += 1
    lmax = int(ecp_in[iline].split()[-1])
    ret_basis += ecp_in[iline]
    # Copy data
    iline += 1 # Skip to next line
    lblock = 0
    while lblock < lmax+1:
        # This should be the definition
        assert len(ecp_in[iline].split()) == 1
        ret_basis += ecp_in[iline]
        lblock += 1
        while True:
            # This should handle the ecp projector data
            iline += 1
            if len(ecp_in[iline].split()) == 1:
                break
            ret_basis += ecp_in[iline]
            print('For Z= {} wrote in ECP line {}'.format(Z, ecp_in[iline]), end='')
            

    iline += 1

ret_basis += '*\n$end'
    
print(ret_basis)
