from addons import *

@ctest_labeler("omp;gradient")
def test_omp2p5_grad2():
    ctest_runner(__file__)

