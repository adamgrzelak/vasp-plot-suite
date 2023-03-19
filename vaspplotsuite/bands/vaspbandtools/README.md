# VASP-Bands-tools
### (C) AG 2022

Library for processing VASP output - loading and selecting band structure

Requires <code>vasprun.xml</code> file.

<code>BandStructure</code> class extracts the entirety of bandstructure data from <code>vasprun.xml</code>.
Its "select" method enables filtering the data by atoms / levels (orbitals/subshells) / spin states
and store them in <code>ProjectedBands</code> class instances.

Can be used as command-line tool or implemented in a different program.
