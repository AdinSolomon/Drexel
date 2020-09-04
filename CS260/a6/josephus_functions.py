#Mark Boady CS 260 - Drexel University 2020
from collections import deque
#Josephus
#Implemented using the builtin list as the queue
def josephus_list(n,m):
	# Initialization of the circle
	circle = []
	i=0
	while i<n:
		circle.append(i)
		i+=1
	results = []
	i=0
	while len(circle)!=0:
		i = (i % m) + 1
		if i == m:
			results.append(circle.pop(0))
		else:
			circle.append(circle.pop(0))
	return results
	
#Implemented using the deque object from collections
def josephus_deque(n,m):
	circle = deque()
	i=0
	while i<n:
		circle.append(i)
		i+=1
	results = deque()
	i=0
	while len(circle)!=0:
		i = (i % m) + 1
		if i == m:
			results.append(circle.popleft())
		else:
			circle.append(circle.popleft())
	return results
