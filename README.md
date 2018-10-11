# Basis Set Exchange - Historical/Provenance Data

This is a collection of historical basis set data used when creating the basis
set exchange (both the original and the newer version)

## Contents

### bse-xml

Data from the original PNNL basis set exchange in XML format. Thanks to
Tara Gibson, Brett Didier, Phil Gackle, and Edo Apra for helping me
obtain and interpret these files.

These files come from the `store/content/files/projects/Basis_Set_Curators/Gaussian`
subdirectory of the BSE source. They have the `_1.0` suffix stripped and are then
compressed. 

### bse-formatted

Actual output of the BSE in the various formats (nwchem, etc). Every basis
set and format combination are here.

Only the basis sets marked 'published' were downloaded.

Obtained 2018-05-09 through 2018-05-10 via a script that downloads from the
BSE website.

### bse-json

The BSE XML converted to JSON through a very convoluted and messy process.
These are being used as the base of the new BSE.


### ccRepo

Data from ccRepo (http://www.grant-hill.group.shef.ac.uk/ccrepo/) in GBASIS format.
Thanks to J. Grant Hill for the data


### GAMESS

Data pulled from GAMESS, either via source or by running test calculations.
Thanks to Ellie Fought for helping obtain this data.


### turbomole

Data from the turbomole project. http://cosmologic-services.de/basis-sets/basissets.php
Obtained September 2018 via that website and via the turbomole packagei (v7.3).

### dalton

Data from the dalton project: https://gitlab.com/dalton/dalton/tree/master

Obtained from commit f08e9f015d226fb904393503e8da22381b8bf851

### gaussian

Basis sets obtained from Gaussian09 Revision E.01 (www.gaussian.com)
