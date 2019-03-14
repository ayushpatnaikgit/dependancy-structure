# dependancy-structure
Visualising C++ dependancy structures 

'graph-generator.py' produces the entire family tree of the reposity and a file name. 'minipath.py' produces the family tree of a particular file. 'dot' files that can used in http://www.webgraphviz.com/ or xdot through the commandline.

#usage
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git <br />
$ cd dependancy-structure <br />
$ python graph-generator.py path_of_src_folder output_file -> for full family tree. <br />
or <br />
$python graph-generator.py path_of_src_folder output_file path_of_child -> for a child's family tree. <br />
$ xdot output_file <br />

#example 
I will use miniqmc repository as an example <br />
$ git clone https://github.com/QMCPACK/miniqmc.git <br />
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git <br />
$ cd dependancy-structure <br />
$ python graph-generator.py ../miniqmc/src example/full_family.dot <br />
$ python graph-generator.py ../miniqmc/src example/miniqmc_family.dot ../miniqmc/src/Drivers/miniqmc.cpp <br />
$ xdot full_family.dot <br />
$ xdot miniqmc_family.dot <br />
here, miniqmc is the repository and src the source folder. <br />

#customizing the tree 

You can play around with the size and the rankseparater to change the dimensions. It might make it easier to visualise. 
