#Mark Boady - Drexel University CS260 2020
#Implement an OPEN hash table
import random

#Hash Functions to test with
def hash1(num,size):
	return num % size
def hash2(num,size):
	x=2*(num**2)+5*num+num
	return x % size
def hash3(num,size):
	word=str(num)
	total=0
	for x in range(0,len(word)):
		c=word[x]
		total=total+ord(c)
		total=total*1010
	return total % size
#Here is a helper function for testing
#It gives you a random sequence
#with no duplicates
def random_sequence(size):
	X=[x for x in range(0,5*size+1)]
	random.shuffle(X)
	return X[0:size]

#The class for the open hash table
class OpenHash:
	#n is the size of the table
	#h_fun is the hash function to use
	#h_fun must be a function that takes two inputs
	#the number to hash and size of the table.
	#It returns an integer between 0 and n-1
	#The index to put the element.
	def __init__(self,n,h_fun):
		self.size = n
		self.data = [ [] for x in range(0,n)]
		self.hash_func = h_fun
	#You can use this str method to help debug
	def __str__(self):
		res=""
		for x in range(0,self.size):
			res+="Row "+str(x)+" "+str(self.data[x])+"\n"
		return res
	#Insert num into the hashtable
	#Do not keep duplicates in the table.
	#If the number is already in the table, do not
	#Insert it again
	def insert(self,num):
		bucket = self.data[self.hash_func(num, self.size)]
		if num not in bucket:
			bucket.append(num)
	#Member returns True is num is in the table
	#It returns False otherwise
	def member(self,num):
		return True if (num in self.data[self.hash_func(num, self.size)]) else False
	#Delete removes num from the table
	def delete(self,num):
		self.data[self.hash_func(num, self.size)].remove(num)
	#You may create any additional
	#Helper methods you wish
