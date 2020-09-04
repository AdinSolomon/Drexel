#Mark Boady
#Drexel University 2020
#CS 260 - Hash Table Homework

import open_hash

def check_at_size(table,size):
	#Insert random elements
	R = open_hash.random_sequence(size)
	for x in R:
		table.insert(x)
	for x in R:
		assert table.member(x)==True
	for x in R:
		table.delete(x)
		assert table.member(x)==False

def test_hash1_simple():
	H=open_hash.OpenHash(5,open_hash.hash1)
	H.insert(9)
	assert H.member(9)==True
	H.delete(9)
	assert H.member(9)==False
def test_hash2_simple():
	H=open_hash.OpenHash(5,open_hash.hash2)
	H.insert(20)
	assert H.member(20)==True
	H.delete(20)
	assert H.member(20)==False
def test_hash3_simple():
	H=open_hash.OpenHash(5,open_hash.hash3)
	H.insert(99)
	assert H.member(99)==True
	H.delete(99)
	assert H.member(99)==False

def test_hash1_ten():
	H=open_hash.OpenHash(10,open_hash.hash1)
	check_at_size(H,10)
def test_hash1_hundred():
	H=open_hash.OpenHash(100,open_hash.hash1)
	check_at_size(H,100)

def test_hash2_ten():
	H=open_hash.OpenHash(10,open_hash.hash2)
	check_at_size(H,10)
def test_hash2_hundred():
	H=open_hash.OpenHash(100,open_hash.hash2)
	check_at_size(H,100)
	
def test_hash3_ten():
	H=open_hash.OpenHash(10,open_hash.hash3)
	check_at_size(H,10)
def test_hash3_hundred():
	H=open_hash.OpenHash(100,open_hash.hash3)
	check_at_size(H,100)

if __name__ == "__main__":
	test_hash1_simple()
	test_hash2_simple()
	test_hash3_simple()
	test_hash1_ten()
	test_hash1_hundred()
	test_hash2_ten()
	test_hash2_hundred()
	test_hash3_ten()
	test_hash3_hundred()
