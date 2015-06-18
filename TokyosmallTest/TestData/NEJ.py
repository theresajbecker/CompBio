

import csv
import json
import sys

Edgecsvfile = open('SmallEdge.csv', 'r')
#creating new to write 
Ejsonfile = open('E2.json', 'wb')

#how to label
Efieldnames = ("source","target","count")
#creating reader 
Ereader = csv.DictReader( Edgecsvfile, Efieldnames)
for row in Ereader:
	edtest = {'data': row}
	json.dump(edtest, Ejsonfile, indent = 3)
Ejsonfile.write('\n')


Nodecsvfile = open('SmallNode.csv', 'r')
Njsonfile = open('N2.json', 'wb')

Nfieldnames = ("source","total_mutations")
Nreader = csv.DictReader( Nodecsvfile, Nfieldnames)
for row in Nreader:
	ndtest = {'data': row}
	json.dump(ndtest, Njsonfile, indent = 2)
Njsonfile.write('\n')




