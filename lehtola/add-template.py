#!/usr/bin/env python3

from basis_set_exchange import curate

guess_sets = {
'grasp_large.gbs': 'sap_grasp_large',
'grasp_small.gbs': 'sap_grasp_small',
'helfem_large.gbs': 'sap_helfem_large',
'helfem_small.gbs': 'sap_helfem_small'
}

hgbs_sets = {
'hgbs-9.gbs': 'HGBS-9',
'hgbsp1-9.gbs': 'HGBSP1-9',
'hgbsp2-9.gbs': 'HGBSP2-9',
'hgbsp3-9.gbs': 'HGBSP3-9',
'ahgbs-9.gbs': 'AHGBS-9',
'ahgbsp1-9.gbs': 'AHGBSP1-9',
'ahgbsp2-9.gbs': 'AHGBSP2-9',
'ahgbsp3-9.gbs': 'AHGBSP3-9'
}

updated_guess_sets = {
'sap_helfem_large.2.gbs': 'sap_helfem_large',
'sap_helfem_small.2.gbs': 'sap_helfem_small'
}

# Lehtola2020a
if False:
    for basis_file, name in hgbs_sets.items():
        curate.add_basis(bs_file=basis_file,
                     data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     subdir='lehtola_hgbs',
                     file_base=name,
                     name=name,
                     family='lehtola_hgbs',
                     role='orbital',
                     description=name,
                     version=1,
                     revision_description='Data from S. Lehtola',
                     data_source='Direct from S. Lehtola',
                     refs='lehtola2020a',
                     file_fmt=None
    )


# Lehtola2020b
if False:
    for basis_file, name in guess_sets.items():
        curate.add_basis(bs_file=basis_file,
                     data_dir='/home/ben/programming/bse_ng/basis_set_exchange/basis_set_exchange/data',
                     subdir='lehtola_sap',
                     file_base=name,
                     name=name,
                     family='lehtola_sap',
                     role='guess',
                     description=name,
                     version=1,
                     revision_description='Data from S. Lehtola',
                     data_source='Direct from S. Lehtola',
                     refs='lehtola2020b',
                     file_fmt=None
    )

for basis_file, name in updated_guess_sets.items():
    curate.add_basis(bs_file=basis_file,
                     data_dir='/home/work/basis_set_exchange/basis_set_exchange/data',
                     subdir='lehtola_sap',
                     file_base=name,
                     name=name,
                     family='lehtola_sap',
                     role='guess',
                     description=f'{name}, recomputed from fractionally-occupied spin-restricted exchange-only LDA references',
                     version=2,
                     revision_description='Data from S. Lehtola',
                     data_source='Direct from S. Lehtola',
                     refs='lehtola2020b',
                     file_fmt=None
    )

        
