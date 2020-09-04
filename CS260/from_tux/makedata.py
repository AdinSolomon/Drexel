# Adin Solomon, abs358@drexel.edu
# CS 260 - Assignment 2

import math
import csv

def f1( x ):
	try:
		return math.pow(x, 3)
	except:
		return "NAN"
def f2( x ):
	try:
		return math.log(x, 2)
	except:
		return "NAN"
def f3( x ):
	try:
		return x * math.log(x, 2)
	except:
		return "NAN"
def f4( x ):
	try:
		return math.pow( 3/2, x)
	except:
		return "NAN"
def f5( x ):
	try:
		return x / math.log(x, 2)
	except:
		return "NAN"
def f6( x ):
	try:
		return math.pow(2, x)
	except:
		return "NAN"
def f7( x ):
	try:
		return math.sqrt(x)
	except:
		return "NAN"
def f8( x ):
	try:
		return math.log( math.log(x, 2), 2 )
	except:
		return "NAN"
def f9( x ):
	try:
		return math.pow(x, 2)
	except:
		return "NAN"
def f10( x ):
	try:
		return x
	except:
		return "NAN"
def f11( x ):
	try:
		return math.pow( math.log(x, 2), 2 )
	except:
		return "NAN"
def f12( x ):
	try:
		return math.pow( 1/3, x )
	except:
		return "NAN"
def allfunctions( x ):
	var =  [x, \
		f1(x),  f2(x),  f3(x),  f4(x), \
		f5(x),  f6(x),  f7(x),  f8(x), \
		f9(x),  f10(x), f11(x), f12(x)]
	return var
def somefunctions( x ):
	var =  [x, \
		f5(x), f7(x), f11(x)]
	return var

if __name__ == "__main__":
	# get data from all the functions
	with open('all-functions.csv', 'w', newline='') as file1:
		w1 = csv.writer(file1)
		# add a header row
		w1.writerow(["x", \
				"x^3",      "log(x)", "x*log(x)",    "(3/2)^x", \
				"x/log(x)", "2^x",     "sqrt(x)",    "log(log(x))", \
				"x^2",      "x",       "(log(x))^2", "(1/3)^x"])
		for x in range(1, 1025):
			try:
				w1.writerow(allfunctions(x))
			except:
				print(x)
				exit(0)
	file1.close()
	# get data from the tails of confusing functions
	with open('some-functions.csv', 'w', newline='') as file2:
		w2 = csv.writer(file2)
		# add a header row
		w2.writerow(["x", \
				"x/log(x)", "sqrt(x)", "(log(x))^2"])
		for x in range(1000000, 1000000000, 1000000):
			w2.writerow(somefunctions(x));
	file2.close()
