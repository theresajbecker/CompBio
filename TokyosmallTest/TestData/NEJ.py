import csv
import json
import sys

#This converts the Node Attribure and Edge Network csv files to the properly formatted Node and Edge json file. 
#Written by Theresa Becker - Summer Training Fellowship 2015- 
#Don't mind the misspelled comments! 
#Happy network visualizing! 





#Open Edge file - Network file - 
Edgecsvfile = open('network3-8-25.csv', 'r')
#creating new/editing output file 
Edgejson = open('network3-8-25.json', 'wb')
#Column Headers for edges
Efieldnames = ("source","target","count")
#creating reader 
Ereader = csv.DictReader( Edgecsvfile, Efieldnames)

#Open Node file - Attributes - 
Nodecsvfile = open('node-attributes.csv', 'r')
#Creating new/editing output file
Nodejson = open('node-attributes.json', 'wb')
#Column headers for node file NODE HEADER MUST CONTAIN ID in order to be recognized by edges
Nfieldnames = ("id","total_mutations")
#Creating Noder reader 
Nreader = csv.DictReader( Nodecsvfile, Nfieldnames)



#Source/Target names are written to holding. Only source/target names contained in holding will be made in to Nodes- 
# aka removes unecessary nodes
holding = []

for row in Ereader:
	#prevents the header line from being created in the network
	if row['source'] == 'source':
		pass
	else:
		#creates a dictionary with key 'data' and value 'row' for each line
		#required to maintain the proper nesting of the json file later
		edtest = {'data': row}
		holding.append(row['source'])
		holding.append(row['target'])
		#json.dump converts the dictionary to a json file (what to write, where to write it, how many columns to indent)
		json.dump(edtest, Edgejson, indent = 3)
#writes to the new file 
print holding
Edgejson.write('\n')


for row in Nreader:
	#if current node id is in holding, it will be written to json for later node creation
	if row['id'] in holding:
		#creates a dictionary with key 'data' and value 'row' for each line
		#required to maintain the proper nesting of the json file later
		ndtest = {'data': row}
		#json.dump converts the dictionary to a json file (what to write, where to write it, how many columns to indent)
		json.dump(ndtest, Nodejson, indent = 2)
	else:
		pass
Nodejson.write('\n')




