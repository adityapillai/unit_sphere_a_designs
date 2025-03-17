from unit_sphere_a_designs import local
import numpy as np
from unit_sphere_a_designs.tools import random_start
import pytest


def test_local_small_d():

    S_val = local.local_search(5, 10)
    alg_val = np.trace( np.linalg.inv( S_val @ S_val.T )  )

    assert alg_val == pytest.approx(2.5, abs=1e-3), "The local search should achieve very close to the optimal value of 2.5 since d=5 is small."

def test_local_fixed_argument():
    # this test cofirms that the local search does not change columns that are fixed in the solution.
    S_start = random_start(5, 10)
    S_alg = local.local_search(5, 10, S_start, fixed_points=[0, 2, 3])

    assert (S_alg[:, [0, 2, 3] ] == pytest.approx(S_start[:, [0, 2, 3] ]))

def test_local_optial_start():
    
    # Below is a optimal solution for d = 5, k = 10. This test confirms that the algortihm does not change make any local moves.
    S_start = np.hstack( [np.eye(5), np.eye(5) ] )
    S_alg = local.local_search(5, 10, S_start)

    assert S_alg == pytest.approx(S_start)