import os
def include_file(x):
    ## creating list of include -> use subprocess call in future to avoid creating temoprary file 
    command = "grep -nr 'include' " + x + "> graph.txt" #creating temporary file
    repository = os.system(command)
    fname = x +"/graph.txt"
    ## OPENING THE FILE THAT INCLUDES THE INCLUDES
    with open(fname) as f:
        repository = f.readlines()
    repository = [x.strip() for x in repository]
    return(repository)
#sys.argv[1] = x