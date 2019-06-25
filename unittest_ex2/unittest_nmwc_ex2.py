#!/bin/python
'''Unittest for the prognostic and diagnostic functions in the isentropic model.
Usage:
Requires:
'''

__author__ = "Daniel Regenass, IACETH"
__contact__ = "daniel.regenass@env.ethz.ch"

import unittest
import numpy as np
import shutil
import time
import os

#we need to move modules before loading functions
print("Copying Functions")
if os.name == 'nt':
    # Windows
    os.system('copy /y ..\prognostics.py prognostics.py')
    os.system('copy /y ..\diagnostics.py diagnostics.py')
else:
    # Linux / MacOS
    shutil.copyfile("../prognostics.py", "prognostics.py")
    shutil.copyfile("../diagnostics.py", "diagnostics.py")

time.sleep(1)


from prognostics import prog_isendens, prog_velocity
from diagnostics import diag_montgomery, diag_pressure
from namelist import nx, nb


class AdiabaticTest(unittest.TestCase):


    @classmethod
    def setUpClass(self, filename='test_data.npz'):
        
        print("\nUNIT TEST FOR THE ADIABATIC MODEL VERSION\n")
        print("\nloading data for test\n")
        self.infile = np.load(filename)
       
        #prognostic variables 
        self.sold = self.infile['sold']
        self.snow = self.infile['snow']
        self.snew_verif = self.infile['snew']
        self.uold = self.infile['uold']
        self.unow = self.infile['unow']
        self.unew_verif = self.infile['unew']

        #diagnostic variables
        self.mtg_old = self.infile['mtg_old']
        self.mtg= self.infile['mtg']
        self.prs_old = self.infile['prs_old']
        self.prs = self.infile['prs']
        self.th0 = self.infile['th0']
        self.exn_old = self.infile['exn_old']
        self.exn = self.infile['exn']
        self.prs0 = self.infile['prs0']

        #other vegetables
        self.dtdx = self.infile['dtdx']
        self.topo = self.infile['topo']
        self.topofact = self.infile['topofact']



    def __assertArrayEqual(self, a, b):

        np.testing.assert_almost_equal(a, b)



    def test_prog_isendens(self):

        snew = prog_isendens(self.sold, self.snow, self.unow, self.dtdx)
        self.__assertArrayEqual(snew[nb:nx+nb, :], self.snew_verif[nb:nx+nb, :])


 
    def test_prog_velocity(self):

        unew = prog_velocity(self.uold, self.unow, self.mtg_old, self.dtdx)
        self.__assertArrayEqual(unew[nb:(nx+1+nb), :], self.unew_verif[nb:(nx+1+nb), :])   


 
    def test_diag_pressure(self):
 
        prs_new = diag_pressure(self.prs0, self.prs_old, self.snew_verif)
        self.__assertArrayEqual(prs_new, self.prs)



    def test_diag_montgomery(self):

        exn_new, mtg_new = diag_montgomery(\
            self.prs, self.mtg_old, self.th0, self.topo, self.topofact)
        self.__assertArrayEqual(exn_new, self.exn)
        self.__assertArrayEqual(mtg_new, self.mtg)



if __name__ == '__main__':

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AdiabaticTest('test_prog_isendens'))
        suite.addTest(AdiabaticTest('test_prog_velocity'))
        suite.addTest(AdiabaticTest('test_diag_pressure'))
        suite.addTest(AdiabaticTest('test_diag_montgomery'))
        return suite

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
