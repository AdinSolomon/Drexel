# Adin Solomon - July 2020
# abs358@drexel.edu
# CS 260 - Assignment 6

import timeit
def josephus_func_test(func_name, n, m):
	setup ="from josephus_functions import josephus_"+func_name+"\n"
	setup+="n = "+str(n)+"\n"
	setup+="m = "+str(m)+"\n"
	test_code = "josephus_"+func_name+"(n, m)"
	t = timeit.timeit(test_code,setup,number=10000)
	return t
	
if __name__ == "__main__":
	n = 1
	m = 2
	print("   N   | List-Based | Deque-Based")
	while n <= 1024:
		list_time = josephus_func_test("list", n, m)
		deque_time = josephus_func_test("deque", n, m)
		print(" %5d | %10f | %10f"%(n, list_time, deque_time))
		n *= 2
