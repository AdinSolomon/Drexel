#Mark Boady
#Drexel University
#CS 260 - Summer 2020

#This function generate a random list of
#size
#It sorts using the given sort_fun
#It then checks that the answer is correct
import random
def check_list(sort_fun,size):
	X=[random.randint(-10*size,10*size) for n in range(0,size)]
	T=X[:]#Make a copy
	sort_fun(T)
	#Is the array sorted?
	for i in range(1,len(T)):
		assert T[i] >= T[i-1]
	#Are all the elements in the list?
	for num in X:
		assert T.count(num)==X.count(num)
	return
	
import sort_code

#Bubble Sort Versions
def test_bubble_ten():
	check_list(sort_code.bubblesort,10)
def test_bubble_hundred():
	check_list(sort_code.bubblesort,100)
def test_bubble_thousand():
	check_list(sort_code.bubblesort,1000)
def test_bubble_fivethousand():
	check_list(sort_code.bubblesort,5000)

#Insertion Sort Version
def test_insert_ten():
	check_list(sort_code.insertion,10)
def test_insert_hundred():
	check_list(sort_code.insertion,100)
def test_insert_thousand():
	check_list(sort_code.insertion,1000)
def test_insert_fivethousand():
	check_list(sort_code.insertion,5000)

#Quick Sort Version
def test_quick_ten():
	check_list(sort_code.quicksort,10)
def test_quick_hundred():
	check_list(sort_code.quicksort,100)
def test_quick_thousand():
	check_list(sort_code.quicksort,1000)
def test_quick_fivethousand():
	check_list(sort_code.quicksort,5000)

#Merge Sort Version
def test_merge_ten():
	check_list(sort_code.mergesort,10)
def test_merge_hundred():
	check_list(sort_code.mergesort,100)
def test_merge_thousand():
	check_list(sort_code.mergesort,1000)
def test_merge_fivethousand():
	check_list(sort_code.mergesort,5000)

if __name__ == "__main__":
	test_merge_ten()
	test_merge_hundred()
	test_merge_thousand()
	test_merge_fivethousand()
	test_quick_ten()
	test_quick_hundred()
	test_quick_thousand()
	test_quick_fivethousand()
