# Python_Crash_Course
#>>>>>>>>>>>>>>> Graph Example  from Video 11 <<<<<<<<<<<<<<<<

graph = {
"0" : ["1","4"],
"1" : ["0","2","3","4"],
"2" : ["1","3"],
"3" : ["1","2","4"],
"4" : ["0","1","3"],
}

def define_edges(connection):
	parosi = []
	for x in connection:
		for y in connection[x]:
			parosi.append((x,y))
	return parosi








#>>>>>>>>>>>>>>> Tree Example  from Video 12 <<<<<<<<<<<<<<<<
class Tree:
	def __init__(self,info,left=None,right=None):
		self.info = info
		self.left = left
		self.right = right


	def __str__(self):
		return (str(self.info) + ', Left Child:' + str(self.left) + ',Right Child:' + str(self.right))


trees = Tree(1, Tree(2,Tree(4,8,9),Tree(5,10,11)), Tree(3,Tree(6,None,13),Tree(7,14,None)))

print(trees)
