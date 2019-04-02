-----------------------------------------------------------------------------
Unit tests for Exercise 2 in Numerical Modelling of Weather and Climate
SS 2019
-----------------------------------------------------------------------------

Debugging the isentropic model can be cumbersome because often one does not
know the initial cause of the wrong result in the output. In order to help 
finding the location of the error(s) this testing routine will execute
4 unit tests:

- prognostic calculation of isentropic density
- prognostic calculation of horizontal density
- diagnostic calculation of pressure
- diagnostic calculation of exner function and montgomery potential

How to use the test:

1) Make sure that this folder (unittest_ex2) is a subfolder of the folder
   containing your source code.

2) Don't modify or delete any files within this folder!

3) Run the unit tests with "python unittest_nmwc_ex2.py" in the console
   or run the corresponding file in Spyder or Ipython.

After running the file you will get a summary of the tests that
succeeded and the ones that failed. If any of the tests failed, the
code in the corresponding function is probably not correct.

Please note that the test does not check any code modifications in
solver.py. So even if all tests succeed, there might still be
something wrong with your modifications to solver.py (e.g. missing
function calls or now update of values for next timestap).

Happy coding :)

The NMWC 2019 tutors:
Christian Zeman     christian.zeman@env.ethz.ch
Christoph Heim      christoph.heim@env.ethz.ch
Daniel Regenass     daniel.regenass@env.ethz.ch
Jörg Wieder         joerg.wieder@env.ethz.ch

