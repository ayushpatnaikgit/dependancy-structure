https://github.com/QMCPACK/miniqmc is used as example 

miniqmc.py is the main file we are looking at so we have generated the it's family tree and the full family tree. 
'
#example I will use miniqmc repository as an example 
$ git clone https://github.com/QMCPACK/miniqmc.git 
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git 
$ cd dependancy-structure 
$ python graph-generator.py ../miniqmc/src example/full_family.dot 
$ python graph-generator.py ../miniqmc/src example/miniqmc_family.dot ../miniqmc/src/Drivers/miniqmc.cpp 
$ xdot full_family.dot 
$ xdot miniqmc_family.dot 

Look at screenshots for results 
