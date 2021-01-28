#!/bin/bash

download() {
    fname=$(echo $f | awk --field-separator=/ '{print $NF}')
    wget -O ${fname} $f && sed -i 's|\r||g;s|\o377||g' ${fname}
}

# Non-relativistic sets
if [[ ! -d nonrel ]]; then
    mkdir nonrel
fi
cd nonrel
for f in $(lynx -dump -listonly http://www.nsc.nagoya-cu.ac.jp/~htatewak/uncontracted_gtf.html|grep http|awk '{print $2}'); do
    download
done
cd ..

# Relativistic sets
if [[ ! -d rel ]]; then
    mkdir rel
fi
cd rel
for f in $(lynx -dump -listonly http://www.nsc.nagoya-cu.ac.jp/~htatewak/uncntrct_rel_gtf.html|grep http|awk '{print $2}'); do
    download
done
cd ..
