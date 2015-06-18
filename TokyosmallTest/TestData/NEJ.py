

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
Nodecsvfile = open('SmallNode.csv', 'r')
Njsonfile = open('N2.json', 'wb')

Nfieldnames = ("source","total_mutations")
Nreader = csv.DictReader( Nodecsvfile, Nfieldnames)

#print "EEEEEEEEEEE reader", Ereader


holding = []

for row in Ereader:
	if row['source'] == 'source':
		pass
	else:
		print "EEEEEE Row", row
		edtest = {'data': row}
		holding.append(row['source'])
		holding.append(row['target'])
		print "HOLDING", holding
		#print edtest
		json.dump(edtest, Ejsonfile, indent = 3)
Ejsonfile.write('\n')


for row in Nreader:
	if row['source'] in holding:
		ndtest = {'data': row}
		json.dump(ndtest, Njsonfile, indent = 2)
	else:
		pass
Njsonfile.write('\n')




