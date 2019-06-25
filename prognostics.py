# -*- coding: utf-8 -*-
import numpy as np
from namelist import imoist, idbg, idthdt, nx, nxb, nb, nz, dth, dt # global variables

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
    for i in range(nb, nx + nb):
        snew[i,:] = sold[i,:]-dtdx*(0.5*snow[i+1,:]*(unow[i+1,:]+unow[i+2,:])-0.5*snow[i-1,:]*(unow[i-1,:]+unow[i,:]))
        if idthdt == 1:
            snew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,1:-2] + dthetadt[i,2:-1])*(snow[i,2:]-snow[i,:-2])

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
    for i in range(nb,nx+nb+1):
        unew[i,:] = uold[i,:] - dtdx*unow[i,:]*(unow[i+1,:]-unow[i-1,:])-2*dtdx*(mtg[i,:]-mtg[i-1,:])
        if idthdt == 1:
            unew[i,1:-1] -= 0.25*dt/dth*(dthetadt[i,1:-2] + dthetadt[i-1,1:-2] + dthetadt[i,2:-1] + dthetadt[i-1,2:-1])*(unow[i,2:]-unow[i,:-2])

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
    u = (unow[1:,:]+unow[:-1,:])/2
    # *** Exercise 4.1/5.2 moisture advection ***
    for i in range(nb,nb+nx):
        qvnew[i,:] = qvold[i,:] - dtdx * u[i,:] * (qvnow[i+1,:] - qvnow[i-1,:])
        qcnew[i,:] = qcold[i,:] - dtdx * u[i,:] * (qcnow[i+1,:] - qcnow[i-1,:])
        qrnew[i,:] = qrold[i,:] - dtdx * u[i,:] * (qrnow[i+1,:] - qrnow[i-1,:])
        if idthdt == 1:
            qvnew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,2:-1] + dthetadt[i,1:-2])*(qvnow[i,2:]-qvnow[i,:-2])
            qcnew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,2:-1] + dthetadt[i,1:-2])*(qcnow[i,2:]-qcnow[i,:-2])
            qrnew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,2:-1] + dthetadt[i,1:-2])*(qrnow[i,2:]-qrnow[i,:-2])

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

    u = (unow[1:,:]+unow[:-1,:])/2
    # *** Exercise 5.1/5.2 number densities ***
    for i in range(nb,nb+nx):
        nrnew[i,:] = nrold[i,:] - dtdx * u[i,:] * (nrnow[i+1,:] - nrnow[i-1,:])
        ncnew[i,:] = ncold[i,:] - dtdx * u[i,:] * (ncnow[i+1,:] - ncnow[i-1,:])

        if idthdt == 1:
            nrnew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,2:-1] + dthetadt[i,1:-2])*(nrnow[i,2:]-nrnow[i,:-2])
            ncnew[i,1:-1] -= 0.5*dt/dth*(dthetadt[i,2:-1] + dthetadt[i,1:-2])*(ncnow[i,2:]-ncnow[i,:-2])

    #
    # *** Exercise 5.1/5.2  *

    return ncnew,nrnew
