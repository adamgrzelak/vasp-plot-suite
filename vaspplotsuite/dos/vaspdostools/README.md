# VASP-DOS-tools
### (C) AG 2022

Library for processing VASP output for plotting eDOS graphs.

Requires <code>vasprun.xml</code> file.

<code>RawDos</code> class extracts the entirety of eDOS data from <code>vasprun.xml</code>.
Its "select" method enables filtering the data by atoms / levels (orbitals/subshells) / spin states
and store them in <code>Dos</code> class instances.

<code>DosPlot</code> is used to produce plots from one or more <code>Dos</code>-type data.

Can be used as command-line tool or implemented in a different program.