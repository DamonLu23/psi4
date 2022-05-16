import pytest

from utils import *

import psi4
import numpy as np
from addons import uusing, using

pytestmark = [pytest.mark.psi, pytest.mark.api]

__potentials = {
    'pna_6w':
    """
@COORDINATES
18
AA
O      9.37100000     2.95300000    -6.07800000       1
H      8.87200000     2.13400000    -6.04900000       2
H      9.87300000     2.94000000    -5.26100000       3
O      7.72000000     5.12000000    -5.51900000       4
H      7.63800000     5.70400000    -6.27600000       5
H      8.29100000     4.41700000    -5.83600000       6
O     10.45300000     3.07700000    -3.43400000       7
H      9.94500000     3.80300000    -3.06600000       8
H     11.35900000     3.30000000    -3.21200000       9
O      6.15200000     4.88500000    -1.44700000      10
H      5.50700000     5.59100000    -1.36900000      11
H      5.89100000     4.42800000    -2.24900000      12
O      5.82300000     3.53700000    -3.94100000      13
H      6.31400000     2.71500000    -4.01100000      14
H      6.27500000     4.12300000    -4.55200000      15
O      8.86000000     5.34600000    -2.74900000      16
H      8.46500000     5.48700000    -3.61200000      17
H      8.10300000     5.25400000    -2.16700000      18
@MULTIPOLES
ORDER 0
18
1      -0.67072060
2       0.33528566
3       0.33543494
4      -0.67055041
5       0.33526795
6       0.33528246
7      -0.67071744
8       0.33530196
9       0.33541547
10     -0.67067328
11      0.33530711
12      0.33536617
13     -0.67033801
14      0.33511794
15      0.33522007
16     -0.67061076
17      0.33527067
18      0.33534009
ORDER 1
18
1       0.00080560    -0.20614866     0.20971724
2       0.12061233     0.19534842    -0.00437020
3      -0.12142692     0.00052018    -0.19496774
4       0.12128208    -0.02952128    -0.26636264
5       0.02123859    -0.14133483     0.17957852
6      -0.13641247     0.16937441     0.07336077
7       0.09874019     0.23525681     0.14626863
8       0.12395337    -0.17250412    -0.08710686
9      -0.21781638    -0.05098712    -0.05185290
10     -0.22463142     0.06171102    -0.17953533
11      0.15306787    -0.16979678    -0.02103891
12      0.06031266     0.11119740     0.19160536
13      0.23374507    -0.05843888    -0.16882627
14     -0.11567937     0.19764719     0.01487010
15     -0.10631260    -0.14219349     0.14548634
16     -0.28549425     0.01213605    -0.06959331
17      0.09187853    -0.03392224     0.20768211
18      0.17941729     0.02239518    -0.14158334
ORDER 2
18
1      -3.82946639     0.38325366     0.37670941    -3.74967413     0.05052330    -3.75455511
2      -0.30950705     0.24207772    -0.02491219    -0.03438601    -0.02932713    -0.45703642
3      -0.30728365    -0.02024246     0.24345483    -0.45782760    -0.02099977    -0.03545985
4      -4.01843560    -0.42071343    -0.05131494    -3.51375485    -0.22366647    -3.80188906
5      -0.45058853    -0.01355906     0.03221603    -0.26454826    -0.26763342    -0.08600138
6      -0.24883865    -0.23689663    -0.12134441    -0.16776157     0.15242467    -0.38450342
7      -3.29787344    -0.20331433    -0.01414521    -3.86392383     0.23538575    -4.17197450
8      -0.32338453    -0.21790162    -0.11343377    -0.11675396     0.16862725    -0.36084577
9       0.03250781     0.14275944     0.13176702    -0.41814694     0.03110778    -0.41507187
10     -3.94275214    -0.29331092     0.07399890    -3.64071323     0.42271528    -3.75038841
11     -0.18497857    -0.27928790    -0.02349247    -0.15879913     0.01388996    -0.45721403
12     -0.40467967     0.08377330     0.14054460    -0.34162736     0.21069480    -0.05454010
13     -3.98817938    -0.10562980    -0.21981136    -3.34423732    -0.30490142    -4.00186338
14     -0.29272797    -0.25436911    -0.02365191    -0.05984813     0.05198185    -0.44875356
15     -0.31577317     0.16791558    -0.17641064    -0.26949266    -0.21058649    -0.21581787
16     -3.76934440     0.01997274    -0.13330175    -4.28009915    -0.16523022    -3.28439494
17     -0.34779244    -0.03700706     0.22659090    -0.43533186    -0.07018391    -0.01780670
18     -0.08414919     0.04219414    -0.26720999    -0.44242465    -0.02713904    -0.27419185
@POLARIZABILITIES
ORDER 1 1
18
1       2.30791521     0.59643991     0.58658837     2.61100398    -0.10257978     2.60785108
2       1.30711897     0.90889808    -0.14203759     2.23138041     0.03064426     0.56363899
3       1.31473738    -0.12335800     0.91322978     0.56426081     0.06343491     2.22049295
4       2.07587445    -0.67088756    -0.21506644     2.80527167    -0.31578724     2.64886958
5       0.72279353     0.00751649     0.24603845     1.44539448    -1.05520399     1.93525324
6       1.51667446    -0.87135876    -0.35833460     1.82612167     0.59796749     0.76044651
7       3.17597352    -0.21979725     0.03827106     2.48641276     0.51074529     1.86433465
8       1.15711080    -0.91546924    -0.49534521     1.87545624     0.51559151     1.06960779
9       2.55558469     0.50338563     0.46922356     0.68876452    -0.02563589     0.85563095
10      2.34307583    -0.51517500     0.28388438     2.61854341     0.61181317     2.56593966
11      1.63329191    -1.01651663    -0.24252266     1.86507920     0.04484738     0.60387225
12      0.76841032     0.41201391     0.40278140     1.14519478     0.81893980     2.18754212
13      2.29130369    -0.22262257    -0.50824047     3.08292101    -0.43438854     2.16011928
14      1.20133160    -0.94148299     0.07075699     2.22478033     0.20477680     0.68049498
15      1.10983723     0.72098321    -0.53040485     1.39825592    -0.82860371     1.59671491
16      2.74369667     0.01646994    -0.12367515     1.60703710    -0.26089660     3.17839863
17      0.86347479    -0.13575237     0.83717068     0.86374986    -0.25419187     2.37549183
18      1.89994613     0.17584219    -1.10556667     0.83549707    -0.08475173     1.36594908
EXCLISTS
18 3
1     2   3
2     1   3
3     1   2
4     5   6
5     4   6
6     4   5
7     8   9
8     7   9
9     7   8
10   11  12
11   10  12
12   10  11
13   14  15
14   13  15
15   13  14
16   17  18
17   16  18
18   16  17
    """,
    'fa_6w':
    """
@COORDINATES
18
AA
O      1.37900000    -1.35200000    -0.48400000       1
H      1.18600000    -0.72200000     0.21400000       2
H      2.29400000    -1.59200000    -0.32400000       3
O      1.42500000     0.33300000    -2.72900000       4
H      1.30700000    -0.34900000    -2.06400000       5
H      1.13400000    -0.08900000    -3.54000000       6
O      4.29400000    -1.30600000     0.06100000       7
H      4.95600000    -1.96300000     0.28600000       8
H      4.29200000    -0.71800000     0.81900000       9
O      3.98200000     2.78500000     0.13700000      10
H      4.09400000     2.22800000    -0.63600000      11
H      4.67200000     3.44400000     0.04300000      12
O      4.16800000     0.93400000    -1.93300000      13
H      3.32100000     0.80000000    -2.36400000      14
H      4.32300000     0.10400000    -1.47700000      15
O      4.04800000     0.63600000     2.07500000      16
H      3.14700000     0.62300000     2.40600000      17
H      4.08600000     1.44400000     1.55900000      18
@MULTIPOLES
ORDER 0
18
1      -0.67045583
2       0.33515422
3       0.33530161
4      -0.67050747
5       0.33519144
6       0.33531603
7      -0.67066479
8       0.33531583
9       0.33534896
10     -0.67089070
11      0.33535776
12      0.33553294
13     -0.67044145
14      0.33519962
15      0.33524183
16     -0.67037463
17      0.33511103
18      0.33526361
ORDER 1
18
1       0.17894445     0.09656937     0.21253723
2       0.04884710    -0.15095807    -0.16593541
3      -0.21893712     0.05923713    -0.03599684
4      -0.10142372    -0.27373245    -0.03627740
5       0.02726784     0.16133126    -0.16093139
6       0.06906228     0.09862369     0.19544604
7       0.16366342    -0.01709409     0.24378024
8      -0.15791510     0.15848298    -0.05139271
9       0.00247103    -0.14225970    -0.18016059
10      0.19898527     0.02538936    -0.21501891
11     -0.02464054     0.13486323     0.18412433
12     -0.16441150    -0.15905255     0.02008407
13     -0.17148359    -0.23892595     0.00621216
14      0.20244137     0.02943083     0.10415918
15     -0.03954998     0.19755020    -0.11007177
16     -0.21363994     0.19691128    -0.04586300
17      0.21495511     0.00564913    -0.08055200
18     -0.01194324    -0.19285216     0.12418791
@POLARIZABILITIES
ORDER 1 1
18
1       2.90095972    -0.48593669     0.06252920     2.25092339     0.62087796     2.38032361
2       0.62174511    -0.24371926    -0.40911109     1.67072095     0.94840430     1.81286002
3       2.61053449    -0.48732062     0.28970806     0.82702180    -0.24083031     0.66489403
4       1.72325126     0.33486576     0.23783027     2.60895950    -0.15361348     3.19876384
5       0.81129923     0.09435729    -0.24402237     1.66781011    -1.11658600     1.62577949
6       0.98737562     0.19941275     0.53774655     0.95398044     0.86196752     2.16123330
7       2.24668082    -0.65013285     0.26630395     2.71820604     0.43662994     2.56274751
8       1.74480064    -0.95949887     0.25678782     1.68682327    -0.43932810     0.67060643
9       0.65540923     0.11878107    -0.11728873     1.47324807     1.03600835     1.97296037
10      2.33555918     0.58665533    -0.27550116     2.66857200     0.53987402     2.51887357
11      0.64903064    -0.26947869    -0.09543050     1.39252746     0.98169315     2.05938551
12      1.80086399     1.01521997    -0.04120678     1.70057782    -0.24242931     0.59621530
13      2.70102584     0.02659006     0.64581219     2.68231281    -0.47790836     2.14923320
14      2.35356456     0.20998540     0.79364949     0.57188772     0.23189383     1.17912767
15      0.62940227    -0.39218205     0.06157844     2.24009742    -0.85280913     1.23428608
16      2.82815510     0.01283732    -0.46076830     2.58053390    -0.63634811     2.12535906
17      2.53931016     0.09662115    -0.67561346     0.57598509     0.11841870     0.99064943
18      0.52378920     0.14388522     0.01748888     2.19896244    -0.90746061     1.38040786
EXCLISTS
18 3
1     2   3
2     1   3
3     1   2
4     5   6
5     4   6
6     4   5
7     8   9
8     7   9
9     7   8
10   11  12
11   10  12
12   10  11
13   14  15
14   13  15
15   13  14
16   17  18
17   16  18
18   16  17 
    """,
    'h2o_spillout':
    """
@COORDINATES
4
AA
O     21.41500000    20.20300000    28.46300000        1
H     20.84000000    20.66500000    29.07300000        2
H     22.26700000    20.19000000    28.89900000        3
X     21.41500000    20.20300000    28.46300000        4
@MULTIPOLES
ORDER 0
4
1       -0.68195912
2        0.34097956
3        0.34097956
4        8.00000000
ORDER 1
4
1        0.07364864     0.11937993     0.27811003
2        0.13201293    -0.10341957    -0.13476149
3       -0.19289612     0.00473166    -0.09514399
4        0 0 0
ORDER 2
4
1       -3.33216702    -0.28299356    -0.01420064    -4.16411766     0.21213644    -3.93180619
2       -0.26788067    -0.15634676    -0.21817674    -0.30867972     0.17884149    -0.20228345
3       -0.01617821     0.00575875     0.24171375    -0.44448719    -0.00422271    -0.31817844
4         0 0 0 0 0 0
@POLARIZABILITIES
ORDER 1 1
4
1        2.98942355    -0.37779481     0.04141173     1.82815813     0.40319255     2.35026343
2        1.31859676    -0.60024842    -0.89358696     1.20607500     0.56785158     1.40652272
3        2.28090986     0.01949959     0.86466278     0.68674835    -0.13216306     0.96339257
4        0 0 0 0 0 0
EXCLISTS
4 4
1       2    3    4
2       1    3    4
3       1    2    4
4       1    2    3
    """,
    'h2s_spillout':
    """
@COORDINATES
4
AA
S     21.41500000    20.20300000    28.46300000        1
H     20.84000000    20.66500000    29.07300000        2
H     22.26700000    20.19000000    28.89900000        3
X     21.41500000    20.20300000    28.46300000        4
@MULTIPOLES
ORDER 0
4
1       -0.68195912
2        0.34097956
3        0.34097956
4        8.00000000
ORDER 1
4
1        0.07364864     0.11937993     0.27811003
2        0.13201293    -0.10341957    -0.13476149
3       -0.19289612     0.00473166    -0.09514399
4        0 0 0
ORDER 2
4
1       -3.33216702    -0.28299356    -0.01420064    -4.16411766     0.21213644    -3.93180619
2       -0.26788067    -0.15634676    -0.21817674    -0.30867972     0.17884149    -0.20228345
3       -0.01617821     0.00575875     0.24171375    -0.44448719    -0.00422271    -0.31817844
4         0 0 0 0 0 0
@POLARIZABILITIES
ORDER 1 1
4
1        2.98942355    -0.37779481     0.04141173     1.82815813     0.40319255     2.35026343
2        1.31859676    -0.60024842    -0.89358696     1.20607500     0.56785158     1.40652272
3        2.28090986     0.01949959     0.86466278     0.68674835    -0.13216306     0.96339257
4        0 0 0 0 0 0
EXCLISTS
4 4
1       2    3    4
2       1    3    4
3       1    2    4
4       1    2    3
    """,
}

__geoms = {
    'pna':
    """
    C          8.64800        1.07500       -1.71100
    C          9.48200        0.43000       -0.80800
    C          9.39600        0.75000        0.53800
    C          8.48200        1.71200        0.99500
    C          7.65300        2.34500        0.05500
    C          7.73200        2.03100       -1.29200
    H         10.18300       -0.30900       -1.16400
    H         10.04400        0.25200        1.24700
    H          6.94200        3.08900        0.38900
    H          7.09700        2.51500       -2.01800
    N          8.40100        2.02500        2.32500
    N          8.73400        0.74100       -3.12900
    O          7.98000        1.33100       -3.90100
    O          9.55600       -0.11000       -3.46600
    H          7.74900        2.71100        2.65200
    H          8.99100        1.57500        2.99500
    """,
    'nh2':
    """
    0 2
    N  0.000000000000     0.000000000000    -0.079859033927
    H  0.000000000000    -0.803611003426     0.554794694632
    H  0.000000000000     0.803611003426     0.554794694632
    """,
    'formamide':
    """
    O     22.931000    21.390000    23.466000
    C     22.287000    21.712000    22.485000
    N     22.832000    22.453000    21.486000
    H     21.242000    21.408000    22.312000
    H     23.729000    22.867000    21.735000
    H     22.234000    23.026000    20.88300
    """,
    'formaldehyde':
    """
    C 2.0092420208996 3.8300915804899 0.8199294419789
    O 2.1078857690998 2.0406638776593 2.1812021228452
    H 2.0682421748693 5.7438044586615 1.5798996515014
    H 1.8588483602149 3.6361694243085 -1.2192956060942
    symmetry c1
    units au
    no_reorient
    no_com
    """
}


def _dump_potential(potname):
    potfile = f'{potname}.pot'
    with open(potfile, 'w') as fp:
        fp.write(__potentials[potname])
    return potfile


@pytest.mark.quick
@uusing("cppe")
def test_cppe_scf_alpha():
    """Tests the PE-SCF ground state energies and static dipole polarizability"""
    alpha_diag = [36.14995, 35.10354, 78.45963]
    ref_pe_energy = -0.03424830892844
    ref_scf_energy = -482.9411084900

    mol = psi4.geometry(__geoms['pna'])
    potfile = _dump_potential('pna_6w')

    psi4.set_options({
        'basis': 'sto-3g',
        'pe': True,
        'e_convergence': 10,
        'd_convergence': 10,
        'scf_type': 'pk',
        'pe__potfile': potfile,
    })
    scf_energy, wfn = psi4.properties("SCF", properties=["DIPOLE_POLARIZABILITIES"], return_wfn=True)
    assert compare_values(ref_pe_energy, wfn.variable("PE ENERGY"), 6, "PE Energy contribution")
    assert compare_values(ref_scf_energy, scf_energy, 6, "Total PE-SCF Energy")
    alpha_ref = [psi4.core.variable(f'DIPOLE POLARIZABILITY {cc}') for cc in ['XX', 'YY', 'ZZ']]
    assert compare_arrays(alpha_diag, alpha_ref, 4, 'PE DIPOLE POLARIZABILITY')


def _base_tdscf_test(molecule, ref_scf_energy, ref_pe_energy, exc_energies, osc_strengths):
    scf_energy, wfn = psi4.energy("TD-SCF", return_wfn=True, molecule=molecule)
    assert compare_values(ref_pe_energy, wfn.variable("PE ENERGY"), 6, "PE Energy contribution")
    assert compare_values(ref_scf_energy, scf_energy, 6, "Total PE-SCF Energy")
    e_calc = []
    r_calc = []
    for i in range(len(exc_energies)):
        e_calc.append(wfn.variable(f'TD-HF ROOT 0 -> ROOT {i+1} EXCITATION ENERGY - A TRANSITION'))
        r_calc.append(wfn.variable(f'TD-HF ROOT 0 -> ROOT {i+1} OSCILLATOR STRENGTH (LEN) - A TRANSITION'))
    assert compare_arrays(exc_energies, e_calc, 4, f'PE EXCITATION ENERGY')
    assert compare_arrays(osc_strengths, r_calc, 4, f'PE OSCILLATOR STRENGTH')


@pytest.mark.quick
@uusing("cppe")
def test_cppe_tdscf_rhf():
    """Tests PE-TDSCF excited states (restricted)"""
    ref_pe_energy = -0.03424830892844
    ref_scf_energy = -482.9411084900
    exc_energies = [0.14366763, 0.15492819, 0.24641827, 0.25335815, 0.25716370]
    osc_strengths = [4.40691123e-06, 8.93210578e-05, 4.32081257e-01, 1.13168661e-01, 1.90262828e-02]

    mol = psi4.geometry(__geoms['pna'])
    potfile = _dump_potential('pna_6w')

    n_states = 5
    psi4.set_options({
        'basis': 'sto-3g',
        'pe': True,
        'e_convergence': 8,
        'd_convergence': 6,
        'scf_type': 'pk',
        'tdscf_states': n_states,
        'pe__potfile': potfile,
    })
    _base_tdscf_test(mol, ref_scf_energy, ref_pe_energy, exc_energies, osc_strengths)


@pytest.mark.quick
@uusing("cppe")
def test_cppe_tdscf_uhf():
    """Tests PE-TDSCF excited states (unrestricted)"""
    ref_pe_energy = -0.0205612607760474
    ref_scf_energy = -54.8574855299258388
    exc_energies = [
        0.10127093659047763, 0.36026243740116887, 0.4991013815039879, 0.5097654655683802, 0.5542193540734713
    ]
    osc_strengths = [
        0.005726019396442727, 1.1052876769210551e-08, 4.1341553724988216e-06, 0.0015188940376984871,
        0.0006496149064569229
    ]

    mol = psi4.geometry(__geoms['nh2'])
    potfile = _dump_potential('pna_6w')

    n_states = 5
    psi4.set_options({
        'basis': 'sto-3g',
        'pe': True,
        'e_convergence': 8,
        'd_convergence': 6,
        'scf_type': 'pk',
        'tdscf_states': n_states,
        'reference': 'uhf',
        'pe__potfile': potfile,
    })
    _base_tdscf_test(mol, ref_scf_energy, ref_pe_energy, exc_energies, osc_strengths)


@pytest.mark.quick
@pytest.mark.ecp
@uusing("ecpint")
@uusing("cppe")
@pytest.mark.parametrize("inp", [
    pytest.param({
        'potname': 'h2o_spillout',
        "ref": -169.106418687201
    }, id='h2o'),
    pytest.param({
        'potname': 'h2s_spillout',
        "ref": -169.104593047406
    }, id='h2s'),
])
def test_cppe_pe_ecp(inp):
    mol = psi4.geometry(__geoms['formamide'])
    potfile = _dump_potential(inp['potname'])
    psi4.set_options({
        'basis': 'aug-cc-pVDZ',
        'pe': True,
        'e_convergence': 10,
        'd_convergence': 10,
        'scf_type': 'pk',
        'pe__potfile': potfile,
        'pe__pe_ecp': True,
    })
    scf_energy, wfn = psi4.energy('scf', return_wfn=True, molecule=mol)
    assert compare_values(inp["ref"], scf_energy, 7, "Total PE-SCF Energy with PE(ECP)")


@pytest.mark.quick
@uusing("cppe")
@uusing("adcc")
def test_pe_adc1():
    """LR-PE-ADC(1)/sto-3g formaldehyde in presence of 6 water molecules
    cross-reference against PE-CIS from Psi4 itself"""
    mol = psi4.geometry(__geoms['formaldehyde'])
    potfile = _dump_potential('pna_6w')
    psi4.set_options({
        'basis': 'sto-3g',
        'pe': True,
        'scf_type': 'pk',
        'pe__potfile': potfile,
        'roots_per_irrep': [5],
        'qc_module': 'adcc',
        'tdscf_states': 5,
        'tdscf_tda': True,
    })
    
    _, wfn_tdhf = psi4.energy('td-hf', return_wfn=True)
    _, wfn_adc = psi4.properties('adc(1)', properties=["oscillator_strength", "dipole"], environment='linear_response', return_wfn=True)

    for i in range(5):
        assert compare_values(wfn_tdhf.variable(f'TD-HF ROOT 0 -> ROOT {i+1} EXCITATION ENERGY'),
                              wfn_adc.variable(f'ADC ROOT 0 -> ROOT {i+1} EXCITATION ENERGY'),
                              5, f"PE-ADC(1) Excitation Energy Root {i+1}")


@uusing("cppe")
@uusing("adcc")
def test_pe_adc2():
    """PE-ADC(2)/cc-pvdz formaldehyde in presence of 6 water molecules
    including ptSS/ptLR corrections for excitation energies
    Reference data from Q-Chem calculation"""
    mol = psi4.geometry(__geoms['formaldehyde'])
    potfile = _dump_potential('fa_6w')
    psi4.set_options({
        'basis': 'cc-pvdz',
        'pe': True,
        'scf_type': 'pk',
        'pe__potfile': potfile,
        'roots_per_irrep': [5],
        'qc_module': 'adcc',
    })
    _, wfn = psi4.properties('adc(2)', properties=["oscillator_strength", "dipole"],
                             environment=True, return_wfn=True)
    energies_uncorrected = [0.15963251547743104, 0.3125861355885466, 0.36222631191059046,
                            0.37972031238708653, 0.4118959244399415]
    pe_ptlr_correction = [-2.9325959339722013e-05, -0.0002702545175242051,
                          -9.683446473705203e-05, -0.0001339512804427152,
                          -0.00270463988662346]
    pe_ptss_correction =  [-0.0005980584740534286, -0.00275711791912612,
                           -0.0008560754671915091, -0.0017443433408762471,
                           -0.0005800145567153289]
    ref_energies = np.array(energies_uncorrected)
    ref_energies += np.array(pe_ptlr_correction) + np.array(pe_ptss_correction)
    
    for i in range(5):
        en = wfn.variable(f"ADC(2) ROOT 0 -> ROOT {i+1} EXCITATION ENERGY")
        assert compare_values(en, ref_energies[i], 5, f"pt-PE-ADC(2) Excitation Energy Root {i+1}")
