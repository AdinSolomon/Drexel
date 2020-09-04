#Mark Boady - CS 260
#Adin Solomon - abs358
#Drexel University 2020

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
	return A

def insertion(A):
	for i in range(1, len(A)):
		j = i
		while j>0 and A[j-1]>A[j]:
			temp = A[j]
			A[j] = A[j-1]
			A[j-1] = temp
			j-=1
	return A

def builtin(A):
	A.sort()
	return A
