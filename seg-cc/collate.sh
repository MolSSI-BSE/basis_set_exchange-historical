#!/bin/bash
# 22 March 2022 Susi Lehtola

symbols=(
    '' 'H' 'He'
    # 2
    'Li' 'Be' 'B' 'C' 'N' 'O' 'F' 'Ne'
    # 3
    'Na' 'Mg' 'Al' 'Si' 'P' 'S' 'Cl' 'Ar'
    # 4
    'K' 'Ca' 'Sc' 'Ti' 'V' 'Cr' 'Mn' 'Fe' 'Co' 'Ni' 'Cu' 'Zn'
    'Ga' 'Ge' 'As' 'Se' 'Br' 'Kr'
    # 5
    'Rb' 'Sr' 'Y' 'Zr' 'Nb' 'Mo' 'Tc' 'Ru' 'Rh' 'Pd' 'Ag' 'Cd'
    'In' 'Sn' 'Sb' 'Te' 'I' 'Xe'
    # 6
    'Cs' 'Ba' 'La' 'Ce' 'Pr' 'Nd' 'Pm' 'Sm' 'Eu' 'Gd' 'Tb' 'Dy'
    'Ho' 'Er' 'Tm' 'Yb' 'Lu'
    'Hf' 'Ta' 'W' 'Re' 'Os' 'Ir' 'Pt' 'Au' 'Hg' 'Tl' 'Pb' 'Bi'
    'Po' 'At' 'Rn'
    # 7
    'Fr' 'Ra' 'Ac' 'Th' 'Pa' 'U' 'Np' 'Pu' 'Am' 'Cm' 'Bk'
    'Cf' 'Es' 'Fm' 'Md' 'No' 'Lr'
    'Rf' 'Db' 'Sg' 'Bh' 'Hs' 'Mt' 'Ds' 'Rg' 'Cn' 'Nh' 'Fl' 'Mc'
    'Lv' 'Ts' 'Og'
)

Zs=({39..48} {72..80})

# Merge the basis sets together
for bas in {,aug-}seg-cc-p{,wc}v{d,t,q,5}z-pp; do
    # Split basis sets
    for Z in ${Zs[@]}; do
        elbas="${symbols[Z]}-${bas}"
        elbas="${elbas,,}"
        if [[ ! -f ${elbas}.txt ]]; then
            echo "${elbas}.txt is missing"
            continue
        fi

        # First and last line of orbital basis
        orbbasbeg=1
        orbbasend=$(awk '{if($1=="END") {print NR}}' ${elbas,,}.txt|head -n 1)
        awk -v begin=${orbbasbeg} -v end=${orbbasend} '{if(NR>begin && NR<end) {print $0}}' ${elbas}.txt > ${elbas}.orb

        # First and last line of ECP definition
        ecpbasbeg=$(awk '{if($1=="ECP") {print NR}}' ${elbas,,}.txt|head -n 1)
        ecpbasend=$(awk '{if($1=="END") {print NR}}' ${elbas,,}.txt|tail -n 1)
        awk -v begin=${ecpbasbeg} -v end=${ecpbasend} '{if(NR>begin && NR<end) {print $0}}' ${elbas}.txt > ${elbas}.ecp
    done

    # Collate
    echo "BASIS \"ao basis\" SPHERICAL PRINT" > ${bas}.nw
    for Z in ${Zs[@]}; do
        elbas="${symbols[Z]}-${bas}"
        elbas="${elbas,,}"
        echo "#BASIS SET: ${bas} ${Z}" >> ${bas}.nw
        cat ${elbas}.orb >> ${bas}.nw
    done
    echo "END" >> ${bas}.nw

    echo "" >> ${bas}.nw
    echo "ECP" >> ${bas}.nw
    for Z in ${Zs[@]}; do
        elbas="${symbols[Z]}-${bas}"
        elbas="${elbas,,}"
        cat ${elbas}.ecp >> ${bas}.nw
    done
    echo "END" >> ${bas}.nw

    # Test conversion
    export PYTHONPATH=/home/work/basis_set_exchange
    python $PYTHONPATH/basis_set_exchange/cli/bse_cli.py convert-basis ${bas}.nw ${bas}.gbs
done

    
