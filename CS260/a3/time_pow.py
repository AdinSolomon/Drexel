import timeit
import csv

#The Normal Python Function
def pow1(a,b):
	return a**b
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow2(a,b):
	total=1
	for i in range(0,b):
		total=total*a
	return total
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow3(a,b):
	if b==0:
		return 1
	elif b%2==1:
		return a*pow3(a,b-1)
	else:
		temp=pow3(a,b//2)
		return temp*temp

def timeyboi(func, a, b):
	try:
		return timeit.timeit(func+'(a, b)', 'from __main__ import '+func+', a, b', number = 10000)
	except:
		return "NAN"

def getrow(a, b):
	return [str(a)+", "+str(b), 
		timeyboi('pow1', a, b),
		timeyboi('pow2', a, b),
		timeyboi('pow3', a, b)]

if __name__ == "__main__":
	with open('pow_timedata.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		# Add a header row
		writer.writerow(['a, b', 'pow1', 'pow2', 'pow3'])
		for a in range(1, 4+1):
			for b in [1, 10, 100, 1000, 10000]:
				print(a, b)
				writer.writerow(getrow(a, b))
