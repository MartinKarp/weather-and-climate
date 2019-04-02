# -*- coding: utf-8 -*-
import numpy as np
from namelist import idbg, idthdt, nx, nxb, nb, nz, dth, dt # global variables

def prog_isendens(sold,snow,unow,dtdx,dthetadt=None):
    """
    Prognostic step for isentropic mass density

    Input:      prog_isendens(sold,snow,unow,dtdx,dthetadt)
    Output:     snew
    """
    if idbg == 1:
        print('Prognostic step: Isentropic mass density ...\n')

    # Declare
    snew = np.zeros((nxb,nz))

    # *** Exercise 2.1/5.2 isentropic mass density ***
    # *** time step for isentropic mass density ***
    # *** edit here ***
    
    

    #
    # *** Exercise 2.1/5.2 isentropic mass density ***

    return snew

def prog_velocity(uold,unow,mtg,dtdx,dthetadt=None):
    """
    Prognostic step for momentum

    Input:      prog_velocity(uold,unow,mtg,dtdx,dthetadt)
    Output:     unew
    """
    if idbg == 1:
        print('Prognostic step: Velocity ...\n')

    # Declare
    unew = np.zeros((nx+1+2*nb,nz))
    
    # *** Exercise 2.1/5.2 velocity ***
    # *** time step for momentum ***
    # *** edit here ***
   
    
    #
    # *** Exercise 2.1/5.2 velocity ***

    return unew

def prog_moisture(unow,qvold,qcold,qrold,
                  qvnow,qcnow,qrnow,qvnew,qcnew,qrnew,dtdx,dthetadt=None):
    """
    Prognostic step for hydrometeors

    Input:      prog_moisture(unow,qvold,qcold,qrold, \
                              qvnow,qcnow,qrnow,qvnew,qcnew,qrnew,dtdx, \
                              dthetadt)
    Output:     qvnew,qcnew,qrnew
    """

    if idbg == 1:
        print('Prognostic step: Moisture scalars ...\n')

    # Declare
    qvnew = np.zeros((nx+2*nb,nz))
    qcnew = np.zeros((nx+2*nb,nz))
    qrnew = np.zeros((nx+2*nb,nz))

    # *** Exercise 4.1/5.2 moisture advection ***
    # *** edit here *** 
    


    #
    # *** Exercise 4.1/5.2  ***
    
    return qvnew,qcnew,qrnew


def prog_numdens(unow,ncold,nrold,ncnow,nrnow,ncnew,nrnew,dtdx,dthetadt=None):
    """
    Prognostic step for number densities

    Input:      prog_numdens(unow,ncold,nrold,ncnow,nrnow,ncnew,nrnew,
                             dthetadt=0)
    Output:     ncnew,nrnew
    """

    if idbg == 1:
       print('Prognostic step: Number densities ...')

    # Declare
    ncnew = np.zeros((nx+2*nb,nz))
    nrnew = np.zeros((nx+2*nb,nz))

    # *** Exercise 5.1/5.2 number densities ***
    # *** edit here *** 



    #
    # *** Exercise 5.1/5.2  *

    return ncnew,nrnew
