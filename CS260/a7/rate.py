# Adin Solomon - July 2020
# abs358@drexel.edu
# CS 260 - Assignment 6

from open_hash import *
import random

TRIALS = 1000

def hash_test(size, hash_func):
	rate = 0
	for i in range(TRIALS):
		h = OpenHash(size, hash_func)
		collisions = 0
		for i in range(size):
			x = int(5*size * random.random())
			if len(h.data[hash_func(x, size)]) != 0:
				collisions += 1
			h.insert(x)
		rate += collisions
	return rate / TRIALS
	
if __name__ == "__main__":
	size = 2
	print("   N   | Hash One | Hash Two | Hash Three")
	while size <= 1024:
		h1 = hash_test(size, hash1)
		h2 = hash_test(size, hash2)
		h3 = hash_test(size, hash3)
		print(" %5d | %8.3f | %8.3f | %8.3f"%(size, h1, h2, h3))
		size *= 2
