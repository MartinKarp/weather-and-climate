# -*- coding: utf-8 -*-
import numpy as np
from namelist import idbg, nz, g, dth, cp, pref, rdcp		# global variables

def diag_montgomery(prs,mtg,th0,topo,topofact):
    """
    Diagnostic computation of Montgomery
    Calculate Exner function and Montgomery potential.
    Based on diag_montgomery.m from the full isentropic model in MATLAB, 2014.

    Input:  diag_montgomery(prs,mtg,th0,topo,topofact)
    Output: exn,mtg
    """
    if idbg == 1:
        print('Diagnostic step: Exner function and Montgomery potential ...\n')

    # *** Exercise 2.2 Diagnostic computation of Montgomery ***
    # *** Calculate Exner function and Montgomery potential ***

    # Computation of Exner function
    # *** Edit here ***


    # add lower boundary condition at height mtg[:,0]
    # *** Edit here ***


    # integration loop upwards
    # *** Edit here ***


    # *** Exercise 2.2 Diagnostic computation  ***

    return exn,mtg


def diag_pressure(prs0,prs,snew):
    """
    Diagnostic computation of pressure
    Diagnostic computation of pressure with upper boundary condition
    and integration downwards.
    Based on diag_pressure.m from the full isentropic model in MATLAB, 2014.

    Input:  diag_pressure(prs0,prs,snew)
    Output: prs
    """
    if idbg == 1:
        print('Diagnostic step: Pressure ...\n')

    # *** Exercise 2.2 Diagnostic computation of pressure ***
    # *** Diagnostic computation of pressure ***
    # *** (upper boundary condition and integration downwards) ***
	
    ## Upper boundary condition
    # *** edit here ***

				
    # integration loop downwards
    # *** edit here ***


    # *** Exercise 2.2 Diagnostic computation of pressure ***

    return prs

# END OF DIAGNOSTICS.PY
