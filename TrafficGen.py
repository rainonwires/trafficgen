import random
import time
from time import gmtime, strftime
import names
#this script generates datasets about traffic, this is fake and not real at all. Just a tool for fun purposes.
import string
import csv

randname = names.get_full_name()
randid = random.randint(0,700000000)
def randplateid (stringLength=5):
	lAD = string.ascii_letters + string.digits
	return ''.join(random.choice(lAD) for i in range (stringLength))
randtime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

print ("1 : console")
whattodo = int(input("how would you like to receive data?: "))
if whattodo == 1:
	print ("Data made at: ", randtime)
	print ("Plate Holder Alias: ", randname)
	print ("ID: ", randid)
	print ("Plate: ", randplateid(7))
else:
	print ("-")
		
		#print ("Plate Holder Alias: ", randname)
		#print ("ID: ", randid)
		#print ("Plate: ", randplateid(7))
		

print ("- github.com/rainonwires/trafficgen -")




