#Mark Boady CS260 - Heap Homework

import random
import time

#Finish Implementation of this Heap

class Heap:
	#Constructor - Do Not Change
	def __init__(self,capacity):
		#How big the Array is
		self.max_size = capacity
		#How many elements in it
		self.current_size = 0
		#The array itself
		self.data = [None]*self.max_size
	#String Method - Do Not Change
	def __str__(self):
		res=""
		res+="Heap Current Size: %d\n"%(self.current_size)
		res+="Heap Max Size: %d\n"%(self.max_size)
		res+="Contents:\n"
		for i in range(0,self.current_size):
			res+="H[%d]=%d\n"%(i,self.data[i])
		res+="\n"
		return res
	#You may Change the Implementation of any function below this line.
	#You may NOT change the signature (input arguments/return value)
	
	#Is the list empty? True/False
	def empty(self):
		return self.current_size == 0
	#What is the min value? Return None if empty
	def min(self):
		return self.data[0]
	#Who is index x's parent?
	def parent(self,x):
		return (x-1) // 2
	#Who is index x's left child?
	def left_child(self,x):
		return 2*x + 1
	#Who is index x's right child?
	def right_child(self,x):
		return 2*x + 2
	#Swap the values at index x and y
	def swap(self,x,y):
		temp = self.data[x]
		self.data[x] = self.data[y]
		self.data[y] = temp
	#Insert a new number x
	#If no space, ignore and make no changes
	def insert(self,x):
		self.data[self.current_size] = x
		self.upheap(self.current_size)
		self.current_size += 1
	#Upheap starting at index i
	def upheap(self,i):
		if self.parent(i) < 0:
			return
		if self.data[i] >= self.data[self.parent(i)]:
			return
		self.swap(i, self.parent(i))
		self.upheap(self.parent(i))
	#Delete the Min and fix heap
	def deletemin(self):
		temp = self.data[0]
		self.swap(0, self.current_size - 1)
		self.current_size -= 1
		self.downheap(0)
		return temp
	#Downheap starting at index i
	def downheap(self,i):
		#print("downheaping on", i)
		#print(self)
		if self.right_child(i) >= self.max_size: # catch segfaults
			#print("\tout of bounds")
			return
		p = self.data[i]
		l = self.data[self.left_child(i)]
		r = self.data[self.right_child(i)]
		l_exists = (l is not None and self.left_child(i) < self.current_size)
		r_exists = (r is not None and self.right_child(i) < self.current_size)
		#print("\tl_exists =", l_exists, ("= "+str(l)) if l_exists else "")
		#print("\tr_exists =", r_exists, ("= "+str(r)) if r_exists else "")
		# ensure no missing children
		if l_exists:
			if r_exists:
				if p < l and p < r:
					return
				elif p < l:
					m = self.right_child(i)
				elif p < r:
					m = self.left_child(i)
				else:
					m = self.left_child(i) if l < r else self.right_child(i)
			elif l < p:
				m = self.left_child(i)
			else:
				return
		else:
			if r_exists:
				if r < p:
					m = self.right_child(i)
				else:
					return
			else:
				return
		self.swap(i, m)
		self.downheap(m)
		
#Implement a Heapsort
def heapsort(A):
	P = Heap(len(A))
	for x in A:
		P.insert(x)
	for i in range(len(A)):
		A[i] = P.min()
		P.deletemin()

if __name__ == "__main__":
	H = Heap(25)
	a = [x+1 for x in range(20)]
	random.shuffle(a)
	a = [3,4,5,1,2]
	print(a)
	for val in a:
		H.insert(val)
	print(H)
	while not H.empty():
		H.deletemin()
		print("ITEM DELTED:")
		print(H)
