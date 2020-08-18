#Mark Boady CS250 - Heap Homework Tests.

import heap
import random

#Real Basics left/right/parent
def test_parent():
    H = heap.Heap(25)
    assert H.parent(10)== 4
    assert H.parent(9) == 4
    assert H.parent(8) == 3
    assert H.parent(7) == 3
    assert H.parent(6) == 2
    assert H.parent(5) == 2
    assert H.parent(4) == 1
    assert H.parent(3) == 1
    assert H.parent(2) == 0
    assert H.parent(1) == 0
def test_left():
    H=heap.Heap(25)
    assert H.left_child(4) == 9
    assert H.left_child(3) == 7
    assert H.left_child(2) == 5
    assert H.left_child(1) == 3
    assert H.left_child(0) == 1
def test_right():
    H=heap.Heap(25)
    assert H.right_child(4) == 10
    assert H.right_child(3) == 8
    assert H.right_child(2) == 6
    assert H.right_child(1) == 4
    assert H.right_child(0) == 2
#Test things that require Insert to work
def test_empty():
    H=heap.Heap(25)
    assert H.empty()==True
    H.insert(10)
    assert H.empty()==False
#Test Basic Min
def test_min():
    H=heap.Heap(25)
    for x in range(10,0,-1):
        H.insert(x)
        assert H.min() == x
#Test Swap Works (Note: this destroys the heap to test)
def test_swap():
    H = heap.Heap(25)
    H.insert(1)
    H.insert(2)
    H.insert(3)
    H.swap(0,2)
    assert H.data[0]==3
    assert H.data[2]==1
#Insert was tested lightly before.
#Test in more detail
#Based on Lecture Slide 19
def test_insert():
    H = heap.Heap(25)
    X=[79, 87, 28, 6, 46, 66, 17, 1, 58, 94]
    for val in X:
        H.insert(val)
    Expected=[1,6,17,28,46,79,66,87,58,94]
    for i in range(0,len(Expected)):
        assert H.data[i] == Expected[i]
#Delete from the Heap
#Also based on slides
def test_delete():
    H=heap.Heap(25)
    X=[79, 87, 28, 6, 46, 66, 17, 1, 58, 94]
    for val in X:
        H.insert(val)
    X.sort()
    pos=0
    while not H.empty():
        min_val = H.min()
        assert min_val == X[pos]
        pos+=1
        H.deletemin()
#Test Sorting
def test_sort_5():
    A = random_array(5)
    Acopy=A[:]
    Acopy.sort()
    heap.heapsort(A)
    for x in range(0,len(Acopy)):
        assert A[x]==Acopy[x]
def test_sort_10():
    A = random_array(10)
    Acopy=A[:]
    Acopy.sort()
    heap.heapsort(A)
    for x in range(0,len(Acopy)):
        assert A[x]==Acopy[x]
def test_sort_100():
    A = random_array(100)
    Acopy=A[:]
    Acopy.sort()
    heap.heapsort(A)
    for x in range(0,len(Acopy)):
        assert A[x]==Acopy[x]
#Helpers for sort
def random_array(size):
    X=[x for x in range(0,5*size)]
    random.shuffle(X)
    return X[0:size]
    
