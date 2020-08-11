import random
from test_avl import *

def gen(n):
	nums = []
	for i in range(n):
		nums.append(random.randint(0, 5*n))
	return make_tree(nums).height()

if __name__ == "__main__":
	print("Elements, Experiment 1, Experiment 2, Experiment 3, Epxeriment 4, Experiment 5, Average")
	x = 16
	for i in range(12):
		n = x * 2**i
		total = 0
		row = str(n) + ","
		for j in range(5):
			exp = gen(n)
			total += exp
			row += str(exp) + ","
		row += str(total / 5)
		print(row)
