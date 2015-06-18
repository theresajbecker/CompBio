
import csv
import json
import sys
from collections import defaultdict
#tree = {}

with open ("E2.json", "r") as myfile:
    Edgedata=myfile.read().replace('\n', '')
    #print "EDGEDATA", Edgedata

with open ("N2.json", "r") as myfile:
    Nodedata=myfile.read().replace('\n', '')
    #print "NODEDATA", Nodedata

    Ndata = Nodedata
    Edata = Edgedata
    print type(Ndata)
    print "Ndata", Ndata
    
    NewNdata = {Ndata}
    print type(NewNdata)

# for i in Ndata.items():
#    	if value not in Edata.values():
#    		pass
#    	else:
#        	NewNdata[key] = value
# print NewNdata

    target =  {"elements" : {'nodes': {Ndata} , 'edges': {Edata}  } }
    #trying something else
    #target =  {"elements" : {'nodes': {{'data': Ndata}}, 'edges':{{'data': Edata}} } }


def set_default(obj):
   if isinstance(obj, set):
      return list(obj)
   raise TypeError

result = json.dumps(target, default=set_default, indent = 1).replace("\\","").replace("}{", "},{").replace("   ", "").replace("\"{", "{").replace("}\"", "}")
#.replace("\"nodes\":", "\"nodes\": [").replace("\"data\": [", "\"data\" :  ").replace("\"edges\":", "\"edges\" : [")
#print result
 

#print json.dumps(target, indent = 3)

f = open( 'DICTTEST.json', 'w' )
f.write(result + '\n' )
f.close()

