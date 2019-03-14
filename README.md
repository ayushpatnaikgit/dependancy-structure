# dependancy-structure
Visualising C++ dependancy structures 

'graph-generator.py' produces the entire family tree of the reposity and a file name. 'minipath.py' produces the family tree of a particular file. 'dot' files that can used in http://www.webgraphviz.com/ or xdot through the commandline.

#usage
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git
$ cd dependancy-structure
$ python graph-generator.py path_of_src_folder output_file -> for full family tree.
or 
$python graph-generator.py path_of_src_folder output_file path_of_child -> for a child's family tree.
$ xdot output_file

#example 
I will use miniqmc repository as an example
$ git clone https://github.com/QMCPACK/miniqmc.git
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git

$ python graph-generator.py ../miniqmc/src example/full_family.dot
$ python graph-generator.py ../miniqmc/src example/miniqmc_family.dot ../miniqmc/src/Drivers/miniqmc.cpp
$ xdot full_family.dot
$ xdot miniqmc_family.dot
here, miniqmc is the repository and src the source folder. 
