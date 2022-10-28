#!/usr/bin/env python3

"""
Test 2d fem code for Poisson equation

Amuthan Ramabathiran
September 2022
"""

import fem_2d_modular as fem
import numpy as np

pi = np.pi


def f(x, y):
    return 8*pi*pi*np.sin(2*pi*x)*np.sin(2*pi*y)


def u_exact(x, y):
    return np.sin(2*pi*x)*np.sin(2*pi*y)


def in_dbc(x, y):
    tol = 1e-6
    if (   abs(x) <= tol or abs(1 - x) <= tol
        or abs(y) <= tol or abs(1 - y) <= tol ):
        return True, 0.0
    else:
        return False, None


n_side = 20
n_quad = 2

nodes, elements, bdy = fem.create_mesh_unit_square(n_side=n_side)
dbc = fem.apply_bc(nodes, elements, bdy, in_dbc)
nbc = None

uh = fem.solve_bvp(nodes, elements, dbc, nbc, n_quad, f)

err_L2 = fem.compute_L2_error_centers(nodes, elements, uh, u_exact)
print(f'L2 error = {err_L2}')
fem.plot_fem_soln(nodes, uh, u_exact, n_plot=21)
