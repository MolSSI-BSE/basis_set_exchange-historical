set -eu

for I in `cat to_parse_basen.txt`; do ../parse.py ../basen "$I" > ${I}.tm; done

# Add ecp for def2
for I in def2-{S,T,Q}*.tm; do cat "${I}" def2-ecp.tm > tmp.xxx; mv tmp.xxx "${I}"; done 


for I in `cat to_parse_jkfit.txt`; do ../parse.py ../jkbasen "$I" > ${I}-JKFIT.tm; done
for I in `cat to_parse_jfit.txt`; do ../parse.py ../jbasen "$I" > ${I}-JFIT.tm; done
for I in `cat to_parse_rifit.txt`; do ../parse.py ../cbasen "$I" > ${I}-RIFIT.tm; done
