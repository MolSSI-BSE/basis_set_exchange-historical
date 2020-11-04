#!/bin/bash

echo $1
for atom in K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe
do
	bc_nwchem.sh xml/$atom.xml $atom > nwchem/$atom.bas
done
