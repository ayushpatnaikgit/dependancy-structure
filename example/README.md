https://github.com/QMCPACK/miniqmc is used as example 

miniqmc.py is the main file we are looking at so we have generated the it's family tree and the full family tree. 
'
#example I will use miniqmc repository as an example 
$ git clone https://github.com/QMCPACK/miniqmc.git <br />
$ git clone https://github.com/ayushpatnaikgit/dependancy-structure.git <br />
$ cd dependancy-structure <br />
$ python graph-generator.py ../miniqmc/src example/full_family.dot <br />
$ python graph-generator.py ../miniqmc/src example/miniqmc_family.dot ../miniqmc/src/Drivers/miniqmc.cpp <br />
$ xdot full_family.dot <br />
$ xdot miniqmc_family.dot <br />

Look at screenshots for results 
