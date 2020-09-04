#Mark Boady - CS 260
#Adin Solomon - abs358
#Drexel University 2020

#util functions
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

#Complete the Following Functions
def bubblesort(A):
	unfinished = True
	while unfinished:
		unfinished = False
		for i in range (1, len(A)):
			if A[i-1]>A[i]:
				temp = A[i]
				A[i] = A[i-1]
				A[i-1] = temp
				unfinished = True

def insertion(A):
	for i in range(1, len(A)):
		j = i
		while j>0 and A[j-1]>A[j]:
			temp = A[j]
			A[j] = A[j-1]
			A[j-1] = temp
			j-=1

def builtin(A):
	A.sort()

def quicksort(A):
	if len(A)<=1:
		return A
	count = 0
	for i in range(len(A)-1):
		if A[i] <= A[-1]:
			swap(A,count,i)
			count+=1
	swap(A,count,-1)
	A[:count] = quicksort( A[:count] )
	A[count:] = quicksort( A[count:] )
	return A

def mergesort(A):
	if (len(A)<=1):
		return A
	B = mergesort( A[:(len(A)//2)] )
	C = mergesort( A[(len(A)//2):] )
	for i in range(len(A)):
		A[i] =  ( B.pop(0) if (len(C)==0) else \
			( C.pop(0) if (len(B)==0) else \
			( B.pop(0) if (B[0]<C[0]) else \
			( C.pop(0) ) ) ) )
	return A

if __name__ == "__main__":
	A = [9,5,6,7,4,3,1,2,4,5,6,6,8,1.5,5,4.5]
	print(quicksort(A[:]))
