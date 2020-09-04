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
	return [a, b, r1, r2, r3]

if __name__ == "__main__":
	# [a, b, pow(a, b)]
	# We're checking when a<0,a=0 and
	# when b<0,b=0,1,2
	# except for when a,b>=0
	# evaluations courtesy of wolframalpha.com
	tests = [[-1, -1, -1], 
		 [-1, 0, 1],
		 [-1, 1, -1],
		 [-1, 2, 1],
		 [0, -1, "inf"]]
	for test in tests:
		fails = ""
		try:
			if pow1(test[0], test[1]) != test[2]:
				fails += "pow1 "
		except:
			fails += "pow1 "
		try:
			if pow2(test[0], test[1]) != test[2]:
				fails += "pow2 "
		except:
			fails += "pow2 "
		try:
			if pow3(test[0], test[1]) != test[2]:
				fails += "pow3 "
		except:
			fails += "pow3 "
		print(fails+"failed test" if len(fails) > 0 else "all three passed test:", test)











