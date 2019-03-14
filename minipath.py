#########################################################################
#Generates family tree of a particular file (child), for the entire source folder
#########################################################################
import sys
from include_file_gen import *
repository = include_file(sys.argv[1])

## opening the file to write the .dot file
dependancy_map = open(sys.argv[2], 'w')
dependancy_map.write("digraph G { \n") # Defining graph G
dependancy_map.write("ranksep = 5 \n") #Rank separator
dependancy_map.write('size = "140,50" \n') #The size of the graph

brackets = ['<','"']
def position(string): #returns the index elements in b in a string. Assuming there is only 1 present
    i = 0
    for x in string:
        if x in brackets:
            break
        i = i + 1
    return(i) 
# system_files = ["stdint.h","ctype.h","getopt.h","inttypes.h","limits.h","string.h","android/log.h","assert.h","sys/time.h","stddef.h","stdio.h","stdarg.h","stdlib.h","Utilities/tinyxml/tinyxml2.h","Utilities/tinyxml/tinyxml2.cpp"]
#you may want to remove system files
link_list = []
def link(x):
    global link_list
    for code in repository:
        # print(code[code.index('/')+1:code.index(':')])
        if x in code[code.index('/')+1:code.index(':')] and code not in link_list:
            # print(code[code.index('/')+1:code.index(':')])
            # continue
        #x = x[x.index('src')+3:] We may need this line in the next version when we don't create the temp file 
            f = (code[0:code.index(':')][::-1])
            try:
                # g = code[code.index('include'):]
                header = code[code.index('include'):]
                if '.hpp' in header:
                    ending = 'pp'
                elif '.cpp' in header:
                    ending = 'pp'
                else:
                    ending = '.h'
                if (f[0:f.index('/')][::-1] + '->' + header[position(header)+1:header.index(ending)+2])[-1]=='>':continue
                k = header[position(header)+1:header.index('.h')+2]
                # if k in system_files:
                #     continue
                edge = '"'+header[position(header)+1:header.index(ending)+2] + '"' + '->' +'"'+ code[code.index('/')+1:code.index(':')]+'"\n'
                dependancy_map.write(edge)
                link_list.append(code)
                link(header[position(header)+1:header.index(ending)+2])
            except:
                continue


#putting a condition for the user to put the entire path for the child file. 
if 'src/' in sys.argv[3]:
    child = sys.argv[3][sys.argv[3].index('src/')+4:]
else:
    child = sys.argv[3]
link(child) #calling the link function that generates the graph

dependancy_map.write("}") #closing the graph
dependancy_map.close




