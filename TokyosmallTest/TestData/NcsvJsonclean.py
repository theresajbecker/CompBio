

import csv
import json
import sys

tree = {}

reader = csv.reader(open(sys.argv[1], 'rb'))
reader.next() 
for row in reader:
    subtree = tree
    for i, cell in enumerate(row):
        if cell:
            if cell not in subtree:
                subtree[cell] = {} if i<len(row)-1 else 1
            subtree = subtree[cell]

print json.dumps(tree, indent=4)








#BEST SOOOOO FAR
#opened small edge to read 
# Edgecsvfile = open('SmallEdge.csv', 'r')
# #creating new to write 
# Ejsonfile = open('E.json', 'wb')

# #how to label
# Efieldnames = ("source","target","count")
# #creating reader 
# Ereader = csv.DictReader( Edgecsvfile, Efieldnames)
# for row in Ereader:
#     json.dump(row, Ejsonfile, indent = 5)
#     Ejsonfile.write('\n')


# Nodecsvfile = open('ExtraNodeData.csv', 'r')
# Njsonfile = open('ExtraNode.json', 'wb')

# Nfieldnames = ("Node", "source","total_mutations")
# Nreader = csv.DictReader( Nodecsvfile, Nfieldnames)
# for row in Nreader:
#     json.dump(row, Njsonfile, indent = 4)
#     Njsonfile.write('\n')
#     print "done"
#testing merge


# z = Ereader.copy()
# z.update(Nreader)

# print z



###############################################

#with open('SmallEdge.csv') as f:

# with open('SmallEdge.csv') as f:
#     reader = csv.reader(f)
#     with open('SmallEdgeDict.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1]:rows[2] for rows in reader}





#     f.readline() # ignore first line (header)

#     mydict = dict(csv.reader(f, delimiter=','))

# print mydict



# with open('coors.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('coors_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}


#d=dict([tuple(line.rstrip('\n').split(",",2)) for line in file('EdgesData.txt')])
#print d 



	# with open('EdgeData.csv', mode='ru') as csvfile:
	# 	reader = csv.DictReader(csvfile)
	# 	with open('EdgeDict.csv', mode='w') as outfile:
	# 		print "reader", reader
	# 		writen =csv.writer(outfile)
	# 		mydict ={rows[0]:rows[1] for rows in reader}
	# 		print mydict
		

# with open('coors.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('coors_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}


#SAVE FOR WHEN CSV IS DICT
		# print 'DATA:', repr(reader)
		# data_string = json.dumps(reader)
		# print 'JSON:', data_string
		# for row in reader:
		# 	#print row
		# 	mydict = {rows[0]:rows[1] for rows in reader}
		# 	print(mydict)





# data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
# print 'DATA:', repr(data)

# data_string = json.dumps(data)
# print 'JSON:', data_string

# 	input_file = csv.DictReader(open("EdgeData.csv"))
# 	for row in input_file:
# 		print row


# with open('coors.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('coors_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}


# with open('names.csv') as csvfile:
# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:
# ...         print(row['first_name'], row['last_name'])
# ...

# if __name__=='__main__':
# 	csvJsonClean()


