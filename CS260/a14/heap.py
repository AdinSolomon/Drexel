#Mark Boady CS260 - Heap Homework

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
        return None
    #What is the min value? Return None if empty
    def min(self):
        return None
    #Who is index x's parent?
    def parent(self,x):
        return None
    #Who is index x's left child?
    def left_child(self,x):
        return None
    #Who is index x's right child?
    def right_child(self,x):
        return None
    #Swap the values at index x and y
    def swap(self,x,y):
        return None
    #Insert a new number x
    #If no space, ignore and make no changes
    def insert(self,x):
        return None
    #Upheap starting at index i
    def upheap(self,i):
        return None
    #Delete the Min and fix heap
    def deletemin(self):
        return None
    #Downheap starting at index i
    def downheap(self,i):
        return None
#Implement a Heapsort
def heapsort(A):
    return None
