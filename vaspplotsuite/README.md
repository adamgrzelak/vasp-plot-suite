# VASP Plot Suite
### (C) AG 2022

Vasp Plot Suite is a program for processing and plotting electronic structure data
from VASP calculations output. It has two modules:

a) DosApp: for plotting electronic density of states (eDOS),<br>
b) BandsApp: for plotting electronic band structure.

Instructions for each of module can be found in their respective README files.

This library is available via pip:
<code>pip install vaspplotsuite</code>

After that, you can run it from your command line by typing <code>vaspplot</code>.

### Executables
This program can be compliled into an executable.
I can provide ones for Windows or MacOS upon request.

### This program is still being tested
If you notice any errors or discrepancies, or if you have any practical suggestions,
I would be grateful if you report them.
I have also included sample data for AgF2 system if you want to give it a try.

### Contact
contact@adamgrzelak.com

### Update history
06.08.2022 - minor refactor<br>
15.05.2022 - updated fonts<br>
13.05.2022 - added command line script<br>
12.05.2022 - publication of version 1.0 Vasp Plot Suite as a whole on PyPI<br>
11.05.2022 - publication of functional BandsApp<br>
10.05.2022 - incorporated <code>matplotlib</code> widget into the main window<br>
05.05.2022 - refactored the application to read <code>vasprun.xml</code><br>
21.03.2022 - incorporated exception handling into vasp-dos-tools and refactored frontend to
display them
