
import csv
import json
import sys
from collections import defaultdict

#This takes the Node Dictionary (JSON) and Edge Dictiontary (JSON) files and combines them in to one multi-nested json file 
#with structure 
#  				Elements 
#			Node 		  Edge
#			/				  \
#		data 				    data
#	/      \				 /  |    \
#  id total_mutations      id  source  target 
#
#Written by Theresa Becker - Summer Training Fellowship 2015- 
#Don't mind the misspelled comments! 
#Happy network visualizing! 


# Opens Edge Json/Dictionary
with open ("network3-8-25.json", "r") as myfile:
    Edgedata=myfile.read().replace('\n', '')

#Opens Node JSON/Dictionary
with open ("node-attributes.json", "r") as myfile:
    Nodedata=myfile.read().replace('\n', '')
    
    #creates multi nested dictionary - which at this point key 'element' has a value which is a set etc
    target =  {"elements" : {'nodes': {Nodedata} , 'edges': {Edgedata}  } }

#this converts the sets to lists in order to make then serializable 
def set_default(obj):
   if isinstance(obj, set):
      return list(obj)
   raise TypeError

#converts the dicts to json and corrects the syntax of the JSON
result = json.dumps(target, default=set_default, indent = 1).replace("\\","").replace("}{", "},{").replace("   ", "").replace("\"{", "{").replace("}\"", "}")

#Writes out the result for your visualizations! 
f = open( 'FinalNetwork3-8-25.json', 'w' )
f.write(result )
f.close()

