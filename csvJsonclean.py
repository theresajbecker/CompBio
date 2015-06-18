import csv
import sys



# def csvJsonClean():
infile = open('EdgeData.csv', 'rU')
reader = csv.reader(infile)
outfile = open('EdgeDataNew', mode = 'w')
writer = csv.writer(outfile)
mydict = {rows[0]:rows[1] for rows in reader}


if __name__=='__main__':
	csvJsonClean()


