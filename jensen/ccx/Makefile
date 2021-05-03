all: ccX01 accX01

ccX00 ccX01 ccX02 ccX03 ccX04: ccX.basis
	csplit -f ccX -z ccX.basis "/Basis set/" '{*}'
	sed -i '/Basis set/d' ccX01
	sed -i '/Basis set/d' ccX02
	sed -i '/Basis set/d' ccX03
	sed -i '/Basis set/d' ccX04
	sed -i '/#/d' ccX01
	sed -i '/#/d' ccX02
	sed -i '/#/d' ccX03
	sed -i '/#/d' ccX04
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' ccX01
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' ccX02
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' ccX03
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' ccX04

accX00 accX01 accX02 accX03 accX04: accX.basis
	csplit -f accX -z ccX.basis "/Basis set/" '{*}'
	sed -i '/Basis set/d' accX01
	sed -i '/Basis set/d' accX02
	sed -i '/Basis set/d' accX03
	sed -i '/Basis set/d' accX04
	sed -i '/#/d' accX01
	sed -i '/#/d' accX02
	sed -i '/#/d' accX03
	sed -i '/#/d' accX04
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' accX01
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' accX02
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' accX03
	sed -i -e 's/^S 1$$/S 1 1.00/g;s/^P 1$$/P 1 1.00/g;s/^D 1$$/D 1 1.00/g;s/^F 1$$/F 1 1.00/g;s/^G 1$$/G 1 1.00/g;s/^H 1$$/H 1 1.00/g' accX04

clean:
	\rm ccX01 ccX02 ccX03 ccX04 accX01 accX02 accX03 accX04 
