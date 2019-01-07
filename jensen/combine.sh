for D in aadmm admm
do
    for I in 0 1 2 3 4 5; do cat ${D}/*-${I}.mol > combined/${D}-${I}.mol; done
done

for D in apcJ apcseg apcSseg apcX pcJ pcseg pcSseg pcX
do
    for I in 0 1 2 3 4 5; do cat ${D}/*-${I}.inp > combined/${D}-${I}.gbs; done
done
