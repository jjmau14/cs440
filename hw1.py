from copy import copy

def breadthFirstSearch(startState, goalState, successorsf):
	bfs = []
	stack = list(startState)
	
	while stack:
		print(stack)
		node = stack.pop(0)
		if node == goalState:
			bfs.append(goalState)
			return bfs
		if not node in bfs:
			bfs.append(node)
			if successorsf(node):
				for child in successorsf(node):
					stack.append(child)
	return bfs
		
	
def depthFirstSearch(start, end, successorsf, visited=[], parentTable={}):
	# Initialize stack with start
	stack = list(start)
	
	# While something is still in the stack
	while stack:
		
		# Pop and visit top of stack
		node = stack.pop()
		visited.append(node)
		
		if successorsf(node):
			for child in successorsf(node):
				if child not in visited:
					stack.append(child)
					parentTable[child] = node

	return getPath(start, end, parentTable)

def getPath(start, end, parents, path=[]):
	node = end
	while node != start:
		path.insert(0, node)
		node = parents[node]
	path.insert(0, start)
	return path
	
successors = {'a': ['b', 'c', 'd'],
 'b': ['e', 'f', 'g'],
 'c': ['a', 'h', 'i'],
 'd': ['j', 'z'],
 'e': ['k', 'l'],
 'g': ['m'],
 'k': ['z']}

def successorsf(state):
	return copy(successors.get(state))	

if __name__ == '__main__':
	print(depthFirstSearch('a', 'z', successorsf))