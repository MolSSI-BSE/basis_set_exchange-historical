# SL 2024-02-20 this file is from the article SI. It uses some nwchem_format function; just define it as a function that returns the string...
def nwchem_format(string, description=""):
    return string

class PAW_L1:
    H = nwchem_format("""
H S
0.124195600556  1.0
H S
0.548796556402  1.0
H S
2.425026804247  1.0
H P
1.294212702504  1.0
""", description="PAW_L1:H")
    Li = nwchem_format("""
Li S
0.047463419332  1.0
Li S
0.209734390251  1.0
Li S
0.926787725648  1.0
Li S
4.095348823728  1.0
Li P
0.609572318398  1.0
Li P
0.115471234968  1.0
""", description="PAW_L1:Li")
    Be = nwchem_format("""
Be S
5.187818453636  1.0
Be S
1.299620922697  1.0
Be S
0.325573178361  1.0
Be S
0.081560624808  1.0
Be P
0.735608407691  1.0
Be P
0.175846529978  1.0
""", description="PAW_L1:Be")
    B = nwchem_format("""
B S
0.116719818632  1.0
B S
0.419416461307  1.0
B S
1.507114816290  1.0
B P
0.090911851473  1.0
B P
0.341950181948  1.0
B P
1.286190139559  1.0
B D
0.429126186446  1.0
""", description="PAW_L1:B")
    C = nwchem_format("""
C S
0.169970578096  1.0
C S
0.619526123585  1.0
C S
2.258112092710  1.0
C P
0.138081087999  1.0
C P
0.512679732685  1.0
C P
1.903522865549  1.0
C D
0.810489468705  1.0
""", description="PAW_L1:C")
    N = nwchem_format("""
N S
0.213991222898  1.0
N S
0.752719627437  1.0
N S
2.647710639043  1.0
N P
0.172666952971  1.0
N P
0.602737346627  1.0
N P
2.104006022967  1.0
N D
0.997823110936  1.0
""", description="PAW_L1:N")
    O = nwchem_format("""
O S
0.274672229174  1.0
O S
0.933989881979  1.0
O S
3.175920267806  1.0
O P
0.191511264287  1.0
O P
0.656943313556  1.0
O P
2.253520276385  1.0
O D
0.957446389167  1.0
""", description="PAW_L1:O")
    F = nwchem_format("""
F S
0.349432541016  1.0
F S
1.180557179987  1.0
F S
3.988510203327  1.0
F P
0.214956322292  1.0
F P
0.716140388110  1.0
F P
2.385866347238  1.0
F D
0.878277585905  1.0
""", description="PAW_L1:F")
    Na = nwchem_format("""
Na S
0.033998628827  1.0
Na S
0.095887391787  1.0
Na S
0.270434197526  1.0
Na S
0.762713990109  1.0
Na S
2.151106021465  1.0
Na P
0.295589627772  1.0
Na P
0.871013568218  1.0
Na P
2.566614538335  1.0
Na P
0.075837001629  1.0
""", description="PAW_L1:Na")
    Mg = nwchem_format("""
Mg S
0.049959557214  1.0
Mg S
0.127738556763  1.0
Mg S
0.326606955580  1.0
Mg S
0.835081483117  1.0
Mg S
2.135169112384  1.0
Mg P
0.367307527255  1.0
Mg P
0.958290236436  1.0
Mg P
2.500139825913  1.0
Mg P
0.106272516233  1.0
""", description="PAW_L1:Mg")
    Al = nwchem_format("""
Al S
0.074498522043  1.0
Al S
0.224245266044  1.0
Al S
0.674992442325  1.0
Al P
0.027925866976  1.0
Al P
0.078177208258  1.0
Al P
0.218853577446  1.0
Al D
0.244570012983  1.0
""", description="PAW_L1:Al")
    Si = nwchem_format("""
Si S
0.101958443132  1.0
Si S
0.307446821943  1.0
Si S
0.927079164990  1.0
Si P
0.037795740705  1.0
Si P
0.106944389047  1.0
Si P
0.302602942429  1.0
Si D
0.299949537829  1.0
""", description="PAW_L1:Si")
    P = nwchem_format("""
P S
0.121826690490  1.0
P S
0.356041605898  1.0
P S
1.040540661663  1.0
P P
0.062168446761  1.0
P P
0.166238177682  1.0
P P
0.444520221411  1.0
P D
0.479498947282  1.0
""", description="PAW_L1:P")
    S = nwchem_format("""
S S
0.144591694682  1.0
S S
0.409941411436  1.0
S S
1.162251823524  1.0
S P
0.081765151618  1.0
S P
0.221561780591  1.0
S P
0.600373406610  1.0
S D
0.531690378634  1.0
""", description="PAW_L1:S")
    Cl = nwchem_format("""
Cl S
0.169851772937  1.0
Cl S
0.473340011699  1.0
Cl S
1.319095837509  1.0
Cl P
0.098757265349  1.0
Cl P
0.268842372589  1.0
Cl P
0.731857256722  1.0
Cl D
0.534625754413  1.0
""", description="PAW_L1:Cl")

class PAW_L2:
    H = nwchem_format("""
H S
0.063460000000  1.0
H S
0.176053000000  1.0
H S
0.488415000000  1.0
H S
1.354984000000  1.0
H S
3.759061000000  1.0
H P
0.451396727538  1.0
H P
1.810087072134  1.0
H D
1.652244513181  1.0
""", description="PAW_L2:H")
    Li = nwchem_format("""
Li S
0.028301188192  1.0
Li S
0.070264893066  1.0
Li S
0.174450456426  1.0
Li S
0.433117598550  1.0
Li S
1.075324524891  1.0
Li S
2.669766450735  1.0
Li P
0.855217037077  1.0
Li P
0.233676428043  1.0
Li P
0.063848906950  1.0
Li D
0.216486368237  1.0
""", description="PAW_L2:Li")
    Be = nwchem_format("""
Be S
0.050418124812  1.0
Be S
0.116451705117  1.0
Be S
0.268970725809  1.0
Be S
0.621246818751  1.0
Be S
1.434905633867  1.0
Be S
3.314228927950  1.0
Be P
1.045729893170  1.0
Be P
0.356640323403  1.0
Be P
0.121630184914  1.0
Be D
0.312273202521  1.0
""", description="PAW_L2:Be")
    B = nwchem_format("""
B S
0.076383510829  1.0
B S
0.210076103481  1.0
B S
0.577768274521  1.0
B S
1.589024993857  1.0
B P
0.055837708774  1.0
B P
0.166375439041  1.0
B P
0.495736435534  1.0
B P
1.477108730307  1.0
B D
0.778111893302  1.0
B D
0.241736491042  1.0
B F
0.656945319854  1.0
""", description="PAW_L2:B")
    C = nwchem_format("""
C S
0.108193719743  1.0
C S
0.301604786675  1.0
C S
0.840764580062  1.0
C S
2.343746221272  1.0
C P
0.082141075776  1.0
C P
0.243838264864  1.0
C P
0.723841255425  1.0
C P
2.148744633440  1.0
C D
1.379530889530  1.0
C D
0.498780052280  1.0
C F
1.069775985753  1.0
""", description="PAW_L2:C")
    N = nwchem_format("""
N S
0.133788379182  1.0
N S
0.361698985855  1.0
N S
0.977858893043  1.0
N S
2.643656886240  1.0
N P
0.094657290335  1.0
N P
0.273165740689  1.0
N P
0.788312465128  1.0
N P
2.274943194225  1.0
N D
0.532216982663  1.0
N D
1.705677297201  1.0
N F
1.518029026379  1.0
""", description="PAW_L2:N")
    O = nwchem_format("""
O S
0.172203433121  1.0
O S
0.451449819095  1.0
O S
1.183524250743  1.0
O S
3.102736102332  1.0
O P
0.094790486900  1.0
O P
0.277663101287  1.0
O P
0.813338978810  1.0
O P
2.382456622377  1.0
O D
0.558660540026  1.0
O D
1.710874019830  1.0
O F
1.365767389299  1.0
""", description="PAW_L2:O")
    F = nwchem_format("""
F S
0.219629004700  1.0
F S
0.573939380338  1.0
F S
1.499831102694  1.0
F S
3.919391862051  1.0
F P
0.093595100241  1.0
F P
0.278650476974  1.0
F P
0.829595653169  1.0
F P
2.469864596071  1.0
F D
0.621891653800  1.0
F D
1.979912786065  1.0
F F
1.226286257486  1.0
""", description="PAW_L2:F")
    Na = nwchem_format("""
Na S
0.034131380539  1.0
Na S
0.096877171538  1.0
Na S
0.274972363170  1.0
Na S
0.780470768367  1.0
Na S
2.215257610810  1.0
Na S
6.287700297240  1.0
Na P
0.315453849944  1.0
Na P
0.549350429049  1.0
Na P
0.956672089910  1.0
Na P
1.666006685747  1.0
Na P
0.072148073947  1.0
Na D
0.283197401959  1.0
""", description="PAW_L2:Na")
    Mg = nwchem_format("""
Mg S
0.049081936952  1.0
Mg S
0.127072321470  1.0
Mg S
0.328988134670  1.0
Mg S
0.851744829255  1.0
Mg S
2.205153249340  1.0
Mg S
5.709105222665  1.0
Mg P
0.475725224096  1.0
Mg P
0.701756493339  1.0
Mg P
1.035181972701  1.0
Mg P
1.527027860486  1.0
Mg P
0.100882995945  1.0
Mg D
0.191913243715  1.0
""", description="PAW_L2:Mg")
    Al = nwchem_format("""
Al S
0.053862961300  1.0
Al S
0.124926752489  1.0
Al S
0.289748151805  1.0
Al S
0.672025725485  1.0
Al P
0.037815493744  1.0
Al P
0.106591886957  1.0
Al P
0.300454370422  1.0
Al P
0.846901497690  1.0
Al D
0.429092037258  1.0
Al D
0.123384836632  1.0
Al F
0.317462584564  1.0
""", description="PAW_L2:Al")
    Si = nwchem_format("""
Si S
0.072740628417  1.0
Si S
0.169475790166  1.0
Si S
0.394855585898  1.0
Si S
0.919959916178  1.0
Si P
0.054727964785  1.0
Si P
0.151032470764  1.0
Si P
0.416803499174  1.0
Si P
1.150250380235  1.0
Si D
0.607561935498  1.0
Si D
0.165430806869  1.0
Si F
0.411176825565  1.0
""", description="PAW_L2:Si")
    P = nwchem_format("""
P S
0.092732037675  1.0
P S
0.204158716556  1.0
P S
0.449475527455  1.0
P S
0.989564654346  1.0
P P
0.071261758032  1.0
P P
0.190988474907  1.0
P P
0.511867775297  1.0
P P
1.371855655237  1.0
P D
0.758115623509  1.0
P D
0.235861473925  1.0
P F
0.581162884572  1.0
""", description="PAW_L2:P")
    S = nwchem_format("""
S S
0.117145464349  1.0
S S
0.243083139136  1.0
S S
0.504410587816  1.0
S S
1.046679099197  1.0
S P
0.085583336359  1.0
S P
0.233512234180  1.0
S P
0.637132949372  1.0
S P
1.738403114509  1.0
S D
0.820479366662  1.0
S D
0.272095682190  1.0
S F
0.591325399074  1.0
""", description="PAW_L2:S")
    Cl = nwchem_format("""
Cl S
0.135503840665  1.0
Cl S
0.275751145120  1.0
Cl S
0.561155268082  1.0
Cl S
1.141954405154  1.0
Cl P
0.104676922523  1.0
Cl P
0.286092258896  1.0
Cl P
0.781918102171  1.0
Cl P
2.137058586838  1.0
Cl D
0.855333662479  1.0
Cl D
0.297772025819  1.0
Cl F
0.580460365437  1.0
""", description="PAW_L2:Cl")


class PAW_L1_contracted:
    H = nwchem_format("""
H S
2.425026804247  0.10712  0.00000
0.548796556402  0.41499  0.00000
0.124195600556  0.60757  1.00000
H P
1.294212702504  1.00000
""", description="PAW_L1_contracted:H")
    Li = nwchem_format("""
Li S
4.095348823728  0.01011 -0.00480  0.00000
0.926787725648 -0.51367 -0.19974  0.00000
0.209734390251 -0.08682  0.04049  0.00000
0.047463419332  0.01155  1.00629  1.00000
Li P
0.609572318398 -0.09743  0.00000
0.115471234968 -0.94987  1.00000
""", description="PAW_L1_contracted:Li")
    Be = nwchem_format("""
Be S
5.187818453636  0.01419 -0.01286  0.00000
1.299620922697 -0.38636 -0.25708  0.00000
0.325573178361 -0.03434  0.29017  0.00000
0.081560624808  0.00399  0.85180  1.00000
Be P
0.735608407691  0.21443  0.00000
0.175846529978  0.85883  1.00000
""", description="PAW_L1_contracted:Be")
    B = nwchem_format("""
B S
1.507114816290  0.17666  0.00000
0.419416461307 -0.47546  0.00000
0.116719818632 -0.68704  1.00000
B P
1.286190139559  0.20786  0.00000
0.341950181948  0.50639  0.00000
0.090911851473  0.48111  1.00000
B D
0.429126186446  1.00000
""", description="PAW_L1_contracted:B")
    C = nwchem_format("""
C S
2.258112092710 -0.16485  0.00000
0.619526123585  0.50339  0.00000
0.169970578096  0.65921  1.00000
C P
1.903522865549  0.23664  0.00000
0.512679732685  0.51325  0.00000
0.138081087999  0.44532  1.00000
C D
0.810489468705  1.00000
""", description="PAW_L1_contracted:C")
    N = nwchem_format("""
N S
2.647710639043  0.08949  0.00000
0.752719627437 -0.56671  0.00000
0.213991222898 -0.57615  1.00000
N P
2.104006022967  0.29603  0.00000
0.602737346627  0.50387  0.00000
0.172666952971  0.37589  1.00000
N D
0.997823110936  1.00000
""", description="PAW_L1_contracted:N")
    O = nwchem_format("""
O S
3.175920267806  0.02768  0.00000
0.933989881979 -0.59145  0.00000
0.274672229174 -0.52871  1.00000
O P
2.253520276385  0.34836  0.00000
0.656943313556  0.49168  0.00000
0.191511264287  0.31307  1.00000
O D
0.957446389167  1.00000
""", description="PAW_L1_contracted:O")
    F = nwchem_format("""
F S
3.988510203327 -0.00183  0.00000
1.180557179987 -0.59542  0.00000
0.349432541016 -0.51521  1.00000
F P
2.385866347238  0.38467  0.00000
0.716140388110  0.46474  0.00000
0.214956322292  0.27118  1.00000
F D
0.878277585905  1.00000
""", description="PAW_L1_contracted:F")
    Na = nwchem_format("""
Na S
2.151106021465  0.03649 -0.01015  0.00000  0.00000
0.762713990109 -0.57729 -0.23401  0.00000  0.00000
0.270434197526 -0.08436 -0.07795  0.00000  0.00000
0.095887391787 -0.00019  0.38794  0.00000  1.00000
0.033998628827  0.00079  0.74620  1.00000  0.00000
Na P
2.566614538335  0.02033
0.871013568218 -0.41802
0.295589627772 -0.14031
Na P
0.075837001629  1.00000
""", description="PAW_L1_contracted:Na")
    Mg = nwchem_format("""
Mg S
2.135169112384  0.04494  0.02023  0.00000  0.00000
0.835081483117 -0.49269  0.34481  0.00000  0.00000
0.326606955580 -0.04548 -0.06937  0.00000  0.00000
0.127738556763 -0.00264 -0.45969  0.00000  1.00000
0.049959557214  0.00080 -0.63253  1.00000  0.00000
Mg P
2.500139825913  0.03595
0.958290236436 -0.36155
0.367307527255 -0.08399
Mg P
0.106272516233  1.00000
""", description="PAW_L1_contracted:Mg")
    Al = nwchem_format("""
Al S
0.674992442325 -0.26445  0.00000
0.224245266044  0.60804  0.00000
0.074498522043  0.62024  1.00000
Al P
0.218853577446  0.40367  0.00000
0.078177208258  0.54906  0.00000
0.027925866976  0.17060  1.00000
Al D
0.244570012983  1.00000
""", description="PAW_L1_contracted:Al")
    Si = nwchem_format("""
Si S
0.927079164990  0.30187  0.00000
0.307446821943 -0.63490  0.00000
0.101958443132 -0.61146  1.00000
Si P
0.302602942429  0.45531  0.00000
0.106944389047  0.52887  0.00000
0.037795740705  0.13542  1.00000
Si D
0.299949537829  1.00000
""", description="PAW_L1_contracted:Si")
    P = nwchem_format("""
P S
1.040540661663  0.22373  0.00000
0.356041605898 -0.70546  0.00000
0.121826690490 -0.52802  1.00000
P P
0.444520221411  0.41534  0.00000
0.166238177682  0.51645  0.00000
0.062168446761  0.19469  1.00000
P D
0.479498947282  1.00000
""", description="PAW_L1_contracted:P")
    S = nwchem_format("""
S S
1.162251823524  0.13870  0.00000
0.409941411436 -0.74253  0.00000
0.144591694682 -0.46674  1.00000
S P
0.600373406610  0.40431  0.00000
0.221561780591  0.51860  0.00000
0.081765151618  0.21262  1.00000
S D
0.531690378634  1.00000
""", description="PAW_L1_contracted:S")
    Cl = nwchem_format("""
Cl S
1.319095837509  0.06280  0.00000
0.473340011699 -0.75278  0.00000
0.169851772937 -0.43177  1.00000
Cl P
0.731857256722  0.42216  0.00000
0.268842372589  0.50707  0.00000
0.098757265349  0.20744  1.00000
Cl D
0.534625754413  1.00000
""", description="PAW_L1_contracted:Cl")

class PAW_L2_contracted:
    H = nwchem_format("""
H S
3.759061000000  0.04480  0.00000  0.00000
1.354984000000  0.12446  0.00000  0.00000
0.488415000000  0.31284  0.00000  0.00000
0.176053000000  0.45780  0.00000  1.00000
0.063460000000  0.20266  1.00000  0.00000
H P
0.451396727538  1.00000
H P
1.810087072134  1.00000
H D
1.652244513181  1.00000
""", description="PAW_L2_contracted:H")
    Li = nwchem_format("""
Li S
2.669766450735  0.03618 -0.00610  0.00000  0.00000
1.075324524891 -0.44517 -0.14488  0.00000  0.00000
0.433117598550 -0.14969 -0.07878  0.00000  0.00000
0.174450456426 -0.02615  0.02055  0.00000  0.00000
0.070264893066  0.00700  0.61390  0.00000  1.00000
0.028301188192 -0.00142  0.45992  1.00000  0.00000
Li P
0.855217037077  0.04716  0.00000
0.233676428043  0.18447  0.00000
0.063848906950  0.86126  1.00000
Li D
0.216486368237  1.00000
""", description="PAW_L2_contracted:Li")
    Be = nwchem_format("""
Be S
3.314228927950 -0.03973 -0.01893  0.00000  0.00000
1.434905633867  0.37221 -0.22092  0.00000  0.00000
0.621246818751  0.06109  0.02415  0.00000  0.00000
0.268970725809  0.01228  0.18486  0.00000  0.00000
0.116451705117 -0.00426  0.56575  0.00000  1.00000
0.050418124812  0.00117  0.35063  1.00000  0.00000
Be P
1.045729893170  0.11881  0.00000
0.356640323403  0.21856  0.00000
0.121630184914  0.77279  1.00000
Be D
0.312273202521  1.00000
""", description="PAW_L2_contracted:Be")
    B = nwchem_format("""
B S
1.589024993857  0.17923  0.00000  0.00000
0.577768274521 -0.23044  0.00000  0.00000
0.210076103481 -0.61252  0.00000  1.00000
0.076383510829 -0.32863  1.00000  0.00000
B P
1.477108730307 -0.15105  0.00000  0.00000
0.495736435534 -0.34879  0.00000  0.00000
0.166375439041 -0.47979  0.00000  1.00000
0.055837708774 -0.23040  1.00000  0.00000
B D
0.778111893302  1.00000
B D
0.241736491042  1.00000
B F
0.656945319854  1.00000
""", description="PAW_L2_contracted:B")
    C = nwchem_format("""
C S
2.343746221272 -0.17397  0.00000  0.00000
0.840764580062  0.27131  0.00000  0.00000
0.301604786675  0.60768  0.00000  1.00000
0.108193719743  0.29913  1.00000  0.00000
C P
2.148744633440 -0.17789  0.00000  0.00000
0.723841255425 -0.37493  0.00000  0.00000
0.243838264864 -0.45336  0.00000  1.00000
0.082141075776 -0.20455  1.00000  0.00000
C D
1.379530889530  1.00000
C D
0.498780052280  1.00000
C F
1.069775985753  1.00000
""", description="PAW_L2_contracted:C")
    N = nwchem_format("""
N S
2.643656886240  0.11003  0.00000  0.00000
0.977858893043 -0.36150  0.00000  0.00000
0.361698985855 -0.57249  0.00000  1.00000
0.133788379182 -0.23454  1.00000  0.00000
N P
2.274943194225 -0.24416  0.00000  0.00000
0.788312465128 -0.40277  0.00000  0.00000
0.273165740689 -0.40071  0.00000  1.00000
0.094657290335 -0.14240  1.00000  0.00000
N D
0.532216982663  1.00000
N D
1.705677297201  1.00000
N F
1.518029026379  1.00000
""", description="PAW_L2_contracted:N")
    O = nwchem_format("""
O S
3.102736102332 -0.05098  0.00000  0.00000
1.183524250743  0.39992  0.00000  0.00000
0.451449819095  0.54228  0.00000  1.00000
0.172203433121  0.20534  1.00000  0.00000
O P
2.382456622377 -0.30417  0.00000  0.00000
0.813338978810 -0.42134  0.00000  0.00000
0.277663101287 -0.34734  0.00000  1.00000
0.094790486900 -0.09182  1.00000  0.00000
O D
0.558660540026  1.00000
O D
1.710874019830  1.00000
O F
1.365767389299  1.00000
""", description="PAW_L2_contracted:O")
    F = nwchem_format("""
F S
3.919391862051  0.02203  0.00000  0.00000
1.499831102694 -0.40289  0.00000  0.00000
0.573939380338 -0.53556  0.00000  1.00000
0.219629004700 -0.19979  1.00000  0.00000
F P
2.469864596071 -0.35350  0.00000  0.00000
0.829595653169 -0.42274  0.00000  0.00000
0.278650476974 -0.29767  0.00000  1.00000
0.093595100241 -0.05658  1.00000  0.00000
F D
0.621891653800  1.00000
F D
1.979912786065  1.00000
F F
1.226286257486  1.00000
""", description="PAW_L2_contracted:F")
    Na = nwchem_format("""
Na S
6.287700297240 -0.00602 -0.00322  0.00000  0.00000  0.00000
2.215257610810  0.05078  0.01440  0.00000  0.00000  0.00000
0.780470768367 -0.57787  0.22306  0.00000  0.00000  0.00000
0.274972363170 -0.09462  0.09255  0.00000  0.00000  1.00000
0.096877171538  0.00218 -0.39103  0.00000  1.00000  0.00000
0.034131380539  0.00008 -0.74823  1.00000  0.00000  0.00000
Na P
1.666006685747  0.07416  0.00000
0.956672089910 -0.44527  0.00000
0.549350429049 -0.00880  0.00000
0.315453849944 -0.15742  1.00000
Na P
0.072148073947  1.00000
Na D
0.283197401959  1.00000
""", description="PAW_L2_contracted:Na")
    Mg = nwchem_format("""
Mg S
5.709105222665  0.00837  0.00776  0.00000  0.00000  0.00000
2.205153249340 -0.06297 -0.03389  0.00000  0.00000  0.00000
0.851744829255  0.50086 -0.32013  0.00000  0.00000  0.00000
0.328988134670  0.04811  0.03816  0.00000  0.00000  1.00000
0.127072321470  0.00326  0.49386  0.00000  1.00000  0.00000
0.049081936952 -0.00112  0.61271  1.00000  0.00000  0.00000
Mg P
1.527027860486  0.18693  0.00000
1.035181972701 -0.64318  0.00000
0.701756493339  0.27326  0.00000
0.475725224096 -0.22694  1.00000
Mg P
0.100882995945  1.00000
Mg D
0.191913243715  1.00000
""", description="PAW_L2_contracted:Mg")
    Al = nwchem_format("""
Al S
0.672025725485  0.28840  0.00000  0.00000
0.289748151805 -0.36180  0.00000  0.00000
0.124926752489 -0.59735  0.00000  1.00000
0.053862961300 -0.29593  1.00000  0.00000
Al P
0.846901497690  0.04050  0.00000  0.00000
0.300454370422 -0.27338  0.00000  0.00000
0.106591886957 -0.56942  0.00000  1.00000
0.037815493744 -0.30768  1.00000  0.00000
Al D
0.429092037258  1.00000
Al D
0.123384836632  1.00000
Al F
0.317462584564  1.00000
""", description="PAW_L2_contracted:Al")
    Si = nwchem_format("""
Si S
0.919959916178  0.32983  0.00000  0.00000
0.394855585898 -0.39217  0.00000  0.00000
0.169475790166 -0.60282  0.00000  1.00000
0.072740628417 -0.28205  1.00000  0.00000
Si P
1.150250380235  0.04806  0.00000  0.00000
0.416803499174 -0.31109  0.00000  0.00000
0.151032470764 -0.56026  0.00000  1.00000
0.054727964785 -0.28112  1.00000  0.00000
Si D
0.607561935498  1.00000
Si D
0.165430806869  1.00000
Si F
0.411176825565  1.00000
""", description="PAW_L2_contracted:Si")
    P = nwchem_format("""
P S
0.989564654346 -0.27411  0.00000  0.00000
0.449475527455  0.48945  0.00000  0.00000
0.204158716556  0.53289  0.00000  1.00000
0.092732037675  0.26374  1.00000  0.00000
P P
1.371855655237  0.02256  0.00000  0.00000
0.511867775297 -0.35448  0.00000  0.00000
0.190988474907 -0.53758  0.00000  1.00000
0.071261758032 -0.25068  1.00000  0.00000
P D
0.758115623509  1.00000
P D
0.235861473925  1.00000
P F
0.581162884572  1.00000
""", description="PAW_L2_contracted:P")
    S = nwchem_format("""
S S
1.046679099197 -0.20176  0.00000  0.00000
0.504410587816  0.55727  0.00000  0.00000
0.243083139136  0.45819  0.00000  1.00000
0.117145464349  0.25862  1.00000  0.00000
S P
1.738403114509 -0.01036  0.00000  0.00000
0.637132949372  0.38081  0.00000  0.00000
0.233512234180  0.53151  0.00000  1.00000
0.085583336359  0.23090  1.00000  0.00000
S D
0.820479366662  1.00000
S D
0.272095682190  1.00000
S F
0.591325399074  1.00000
""", description="PAW_L2_contracted:S")
    Cl = nwchem_format("""
Cl S
1.141954405154  0.11248  0.00000  0.00000
0.561155268082 -0.58065  0.00000  0.00000
0.275751145120 -0.43148  0.00000  1.00000
0.135503840665 -0.22338  1.00000  0.00000
Cl P
2.137058586838  0.01181  0.00000  0.00000
0.781918102171 -0.39510  0.00000  0.00000
0.286092258896 -0.52102  0.00000  1.00000
0.104676922523 -0.22922  1.00000  0.00000
Cl D
0.855333662479  1.00000
Cl D
0.297772025819  1.00000
Cl F
0.580460365437  1.00000
""", description="PAW_L2_contracted:Cl")

class PAW_L0_5:
    H = nwchem_format("""
H S
1.200891000000  1.0
H S
0.179946000000  1.0
H P
0.416735075677  1.0
""", description="PAW_L0_5:H")
    Li = nwchem_format("""
Li S
0.046288576701  1.0
Li S
0.203730311817  1.0
Li S
0.896679978314  1.0
Li P
0.591111438159  1.0
Li P
0.113890225864  1.0
""", description="PAW_L0_5:Li")
    Be = nwchem_format("""
Be S
0.078869772268  1.0
Be S
0.315578166553  1.0
Be S
1.262709100605  1.0
Be P
0.730673772563  1.0
Be P
0.176505218767  1.0
""", description="PAW_L0_5:Be")
    B = nwchem_format("""
B S
0.063212346810  1.0
B S
0.203964163981  1.0
B P
0.166604249662  1.0
B P
0.904389402717  1.0
O D
0.411811189773  1.0
""", description="PAW_L0_5:B")
    C = nwchem_format("""
C S
0.100017381477  1.0
C S
0.328305910981  1.0
C P
0.262412581466  1.0
C P
1.405886265616  1.0
C D
0.761923398467  1.0
""", description="PAW_L0_5:C")
    N = nwchem_format("""
N S
0.166676610017  1.0
N S
0.548648300184  1.0
N P
0.339491756443  1.0
N P
1.704706733319  1.0
N D
0.965354217499  1.0
""", description="PAW_L0_5:N")
    O = nwchem_format("""
O S
0.255318792316  1.0
O S
0.850799102076  1.0
O P
0.393300708207  1.0
O P
1.925061049139  1.0
O D
0.943815637381  1.0
""", description="PAW_L0_5:O")
    F = nwchem_format("""
F S
0.348871554099  1.0
F S
1.189620120262  1.0
F P
0.448675119907  1.0
F P
2.109735258087  1.0
F D
0.836842749037  1.0
""", description="PAW_L0_5:F")
    Na = nwchem_format("""
Na S
0.033655350373  1.0
Na S
0.092196449631  1.0
Na S
0.252565646481  1.0
Na S
0.691885707503  1.0
Na P
0.718252994538  1.0
Na P
0.139581056435  1.0
""", description="PAW_L0_5:Na")
    Mg = nwchem_format("""
Mg S
0.054842942010  1.0
Mg S
0.132477377733  1.0
Mg S
0.320009375276  1.0
Mg S
0.773007452422  1.0
Mg P
0.800217847633  1.0
Mg P
0.145480134515  1.0
""", description="PAW_L0_5:Mg")
    Al = nwchem_format("""
Al S
0.032498891201  1.0
Al S
0.114560526116  1.0
Al P
0.055825481446  1.0
Al P
0.193518642332  1.0
Al D
0.229482808566  1.0
""", description="PAW_L0_5:Al")
    Si = nwchem_format("""
Si S
0.041194032014  1.0
Si S
0.154293469475  1.0
Si P
0.081556470376  1.0
Si P
0.277139451681  1.0
Si D
0.286262749529  1.0
""", description="PAW_L0_5:Si")
    P = nwchem_format("""
P S
0.068231681068  1.0
P S
0.222795990837  1.0
P P
0.115290420342  1.0
P P
0.393725303142  1.0
P D
0.466520923939  1.0
""", description="PAW_L0_5:P")
    S = nwchem_format("""
S S
0.103703800041  1.0
S S
0.308231638601  1.0
S P
0.146815153676  1.0
S P
0.522350376343  1.0
S D
0.531591879932  1.0
""", description="PAW_L0_5:S")
    Cl = nwchem_format("""
Cl S
0.144208209347  1.0
Cl S
0.409342667533  1.0
Cl P
0.180330399132  1.0
Cl P
0.645700679971  1.0
Cl D
0.529731610862  1.0
""", description="PAW_L0_5:Cl")