#Mark Boady CS 260 - Drexel University 2020
import josephus_functions
import pytest
#Known Answers
def known_answers(n,m):
	D={}
	D[(2,2)]=[1, 0]
	D[(5,2)]=[1, 3, 0, 4, 2]
	D[(5,3)]=[2, 0, 4, 1, 3]
	D[(7,2)]=[1, 3, 5, 0, 4, 2, 6]
	D[(7,3)]=[2, 5, 1, 6, 4, 0, 3]
	D[(10,2)]=[1, 3, 5, 7, 9, 2, 6, 0, 8, 4]
	D[(10,3)]=[2, 5, 8, 1, 6, 0, 7, 4, 9, 3]
	D[(10,5)]=[4, 9, 5, 1, 8, 7, 0, 3, 6, 2]
	D[(100,2)]=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 0, 16, 32, 48, 64, 80, 96, 24, 56, 88, 40, 8, 72]
	D[(100,10)]=[9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 23, 35, 47, 60, 72, 84, 96, 8, 24, 37, 51, 64, 78, 92, 5, 20, 36, 52, 67, 82, 97, 14, 30, 46, 63, 81, 0, 16, 34, 55, 73, 91, 12, 31, 53, 74, 94, 17, 41, 62, 86, 7, 38, 61, 88, 15, 44, 71, 2, 28, 66, 95, 27, 68, 3, 42, 80, 22, 58, 6, 56, 4, 57, 18, 77, 40, 1, 83, 50, 45, 33, 48, 75, 93, 70, 26, 90, 13, 85, 25]
	K=(n,m)
	if K in D.keys():
		return D[K]
	else:
		return []
		
def compare(A,B):
	assert len(A)==len(B)
	for x in range(0,len(A)):
		assert A[x]==B[x]
		
#Tests
def test_jlist_2_2():
	x=josephus_functions.josephus_list(2,2)
	y=known_answers(2,2)
	compare(x,y)
def test_jdeque_2_2():
	x=josephus_functions.josephus_deque(2,2)
	y=known_answers(2,2)
	compare(x,y)
	
def test_jlist_5_2():
	x=josephus_functions.josephus_list(5,2)
	y=known_answers(5,2)
	compare(x,y)
def test_jdeque_5_2():
	x=josephus_functions.josephus_deque(5,2)
	y=known_answers(5,2)
	compare(x,y)
	
def test_jlist_5_3():
	x=josephus_functions.josephus_list(5,3)
	y=known_answers(5,3)
	compare(x,y)
def test_jdeque_5_3():
	x=josephus_functions.josephus_deque(5,3)
	y=known_answers(5,3)
	compare(x,y)
	
	
def test_jlist_7_2():
	x=josephus_functions.josephus_list(7,2)
	y=known_answers(7,2)
	compare(x,y)
def test_jdeque_7_2():
	x=josephus_functions.josephus_deque(7,2)
	y=known_answers(7,2)
	compare(x,y)
	
def test_jlist_7_3():
	x=josephus_functions.josephus_list(7,3)
	y=known_answers(7,3)
	compare(x,y)
def test_jdeque_7_3():
	x=josephus_functions.josephus_deque(7,3)
	y=known_answers(7,3)
	compare(x,y)
	
def test_jlist_10_2():
	x=josephus_functions.josephus_list(10,2)
	y=known_answers(10,2)
	compare(x,y)
def test_jdeque_10_2():
	x=josephus_functions.josephus_deque(10,2)
	y=known_answers(10,2)
	compare(x,y)
	
def test_jlist_10_3():
	x=josephus_functions.josephus_list(10,3)
	y=known_answers(10,3)
	compare(x,y)
def test_jdeque_10_3():
	x=josephus_functions.josephus_deque(10,3)
	y=known_answers(10,3)
	compare(x,y)
	
def test_jlist_10_5():
	x=josephus_functions.josephus_list(10,5)
	y=known_answers(10,5)
	compare(x,y)
def test_jdeque_10_5():
	x=josephus_functions.josephus_deque(10,5)
	y=known_answers(10,5)
	compare(x,y)
	
def test_jlist_100_2():
	x=josephus_functions.josephus_list(100,2)
	y=known_answers(100,2)
	compare(x,y)
def test_jdeque_100_2():
	x=josephus_functions.josephus_deque(100,2)
	y=known_answers(100,2)
	compare(x,y)
	
def test_jlist_100_10():
	x=josephus_functions.josephus_list(100,10)
	y=known_answers(100,10)
	compare(x,y)
def test_jdeque_100_10():
	x=josephus_functions.josephus_deque(100,10)
	y=known_answers(100,10)
	compare(x,y)

if __name__ == "__main__":
	test_jlist_2_2()
	test_jdeque_2_2()
	test_jlist_5_2()
	test_jdeque_5_2()
	test_jlist_5_3()
	test_jdeque_5_3()
	test_jlist_7_2()
	test_jdeque_7_2()
	test_jlist_7_3()
	test_jdeque_7_3()
	test_jlist_10_2()
	test_jdeque_10_2()
	test_jlist_10_3()
	test_jdeque_10_3()
	test_jlist_10_5()
	test_jdeque_10_5()
	test_jlist_100_2()
	test_jdeque_100_2()
	test_jlist_100_10()
	test_jdeque_100_10()

