
#Mark Boady
#CS 260
#Binary Search Tree w/ Pointers

class node:
	def __init__(self,v,l=None,r=None,nh=0):
		self.value = v
		self.left = l
		self.right = r
		self.nodeHeight = nh
	def __str__(self):
		return str(self.value)
	def getValue(self):
		return self.value
	def setValue(self,v):
		self.value=v
	def getLeft(self):
		return self.left
	def setLeft(self,l):
		self.left = l
	def getRight(self):
		return self.right
	def setRight(self,r):
		self.right = r
	def getNodeHeight(self):
		return self.nodeHeight
	def setNodeHeight(self, nh):
		self.nodeHeight = nh

class AVL:
	def __init__(self):
		self.root=None
	def __str__(self):
		return self.inorder()
	#ADT Interface
	#These don't do much. They just set the correct inputs.
	def getRoot(self):
		return self.root
	def insert(self,value):
		self.root = self.insert_value(value, \
			self.root)
	def find(self,value):
		return self.find_value(value,self.root)
	def delete(self,value):
		self.root=self.delete_value(value, \
			self.root)
	def min(self):
		return self.find_min(self.getRoot())
	def inorder(self):
		return self.inorder_walk(self.root)
	def preorder(self):
		return self.preorder_walk(self.root)
	def postorder(self):
		return self.postorder_walk(self.root)
	def height(self):
		return self.getHeight(self.root)
	def getHeight(self, node):
		if node == None:
			return -1
		return node.getNodeHeight()
	def balance(self):
		return self.getBalance(self.root)
	def getBalance(self, node):
		if node == None:
			return -1
		l = self.getHeight(node.getLeft())
		r = self.getHeight(node.getRight())
		return l - r
	def updateHeight(self, node):
		l = self.getHeight(node.getLeft())
		r = self.getHeight(node.getRight())
		h = 1 + max(l, r)
		node.setNodeHeight(h)
	def leftRotate(self, x):
		y = x.getRight()
		x.setRight(y.getLeft())
		y.setLeft(x)
		self.updateHeight(x)
		self.updateHeight(y)
		return y
	def rightRotate(self, y):
		x = y.getLeft()
		y.setLeft(x.getRight())
		x.setRight(y)
		self.updateHeight(y)
		self.updateHeight(x)
		return x
	def rebalance(self, node, value):
		balance = self.getBalance(node)
		if balance > 1 and value < node.getLeft().getValue():
			return self.rightRotate(node)
		elif balance > 1 and value > node.getLeft().getValue():
			node.setLeft(self.leftRotate(node.getLeft()))
			return self.rightRotate(node)
		elif balance < -1 and value > node.getRight().getValue():
			return self.leftRotate(node)
		elif balance < -1 and value < node.getRight().getValue():
			node.setRight(self.rightRotate(node.getRight()))
			return self.leftRotate(node)
		return node
	#Recursive definition for insert
	def insert_value(self,value,mynode):
		#Implement me
		if mynode == None:
			return node(value)
		elif value == mynode.getValue():
			return mynode
		elif value < mynode.getValue():
			mynode.setLeft(self.insert_value(value, mynode.getLeft()))
		else:
			mynode.setRight(self.insert_value(value, mynode.getRight()))
		self.updateHeight(mynode)
		mynode = self.rebalance(mynode, value)
		return mynode
	#Search Function
	def find_value(self,value,mynode):
		#Implement Me
		if mynode == None:
			return False
		if value == mynode.getValue():
			return True
		if value < mynode.getValue():
			return self.find_value(value, mynode.getLeft())
		return self.find_value(value, mynode.getRight())
	#Display Functions
	#Inorder Walk
	def inorder_walk(self,mynode):
		#Implement Me
		if mynode == None:
			return "N"
		return self.inorder_walk(mynode.getLeft()) +  " " + \
			str(mynode.getValue()) + " " + \
			self.inorder_walk(mynode.getRight())
	#Preorder Walk
	def preorder_walk(self,mynode):
		#Implement Me
		if mynode == None:
			return "N"
		return str(mynode.getValue()) + " " + \
			self.preorder_walk(mynode.getLeft()) + " " + \
			self.preorder_walk(mynode.getRight())
	#Post Order
	def postorder_walk(self,mynode):
		#Implement Me
		if mynode == None:
			return "N"
		return self.postorder_walk(mynode.getLeft()) + " " + \
			self.postorder_walk(mynode.getRight()) + " " + \
			str(mynode.getValue())
	#Delete From Tree
	#Recursive Definition (Works if you implement find min correctly)
	def delete_value(self,value,mynode):
		#Thing to delete not found
		if mynode==None:
			return None
		#Found Node to Delete
		elif mynode.getValue()==value:
			#If either side is null
			#Move up other side
			if mynode.getLeft()==None:
				return mynode.getRight()
			elif mynode.getRight()==None:
				return mynode.getLeft()
			#Otherwise reorganize!
			else:
				#Find Smallest Value on Right Side
				minval = self.find_min(\
					mynode.getRight())
				#Swap to this position
				mynode.setValue(minval)
				#Remove that value
				#We know it has no left child
				new_right = self.delete_value(\
					minval,mynode.getRight())
				#Update Pointers
				mynode.setRight(new_right)
				return mynode
		#Search More
		elif mynode.getValue() > value:
			mynode.setLeft(\
				self.delete_value(\
					value,mynode.getLeft()))
			return mynode
		else:
			mynode.setRight(\
				self.delete_value(\
					value,mynode.getRight()))
			return mynode
	#Find Min
	def find_min(self,mynode):
		#Implement Me
		if mynode == None:
			return None
		elif mynode.getLeft() == None:
			return mynode.getValue()
		else:
			return self.find_min(mynode.getLeft())
	def node_height(self,mynode):
		#Implement Me
		if self.getRoot() == None:
			return 0
		if mynode == None:
			return -1
		l = self.node_height(mynode.getLeft())
		r = self.node_height(mynode.getRight())
		return 1 + (l if l > r else r)
	def update(self):
		updateHeights(self, self.root)

if __name__=="__main__":
	t = AVL()
	print(t.getRoot())
	t.insert
	to_insert=[5,3,4,2,7,9,6]
	print("A simple set of BST Examples.")
	my_tree = AVL()
	for x in to_insert:
		print("inserting", x)
		my_tree.insert(x)
		print("Tree After Insert "+str(x))
		print("Inorder:")
		print(my_tree.inorder())
		print("Preorder:")
		print(my_tree.preorder())
		print("Postorder:")
		print(my_tree.postorder())
	print("The height of the tree is",my_tree.height())
	for x in range(0,13):
		print("Is "+str(x)+" in the tree? "+str(my_tree.find(x)))
