# Adin Solomon - July 2020
# abs358@drexel.edu
# CS 260 - Assignment 6

import josephus_functions

tests = [
	[7,  2,  [1,3,5,0,4,2,6]],
	[7,  3,  [2,5,1,6,4,0,3]],
	[10, 2,  [1,3,5,7,9,2,6,0,8,4]],
	]

def test_list():
	for test in tests:
		if josephus_functions.josephus_list(test[0], test[1]) != test[2]:
			print("list function failed test:", test, "\n\twith result", josephus_functions.josephus_list(test[0],test[1]))

def test_deque():
	for test in tests:
		if josephus_functions.josephus_deque(test[0], test[1]) != test[2]:
			print("deque function failed test:", test, "\n\twith result", josephus_functions.josephus_deque(test[0],test[1]))

if __name__ == "__main__":
	test_list()
	test_deque()
