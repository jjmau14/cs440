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
		
	
def depthFirstSearch(start, end, successorsf):
	# Initialize stack with source node
	stack = list(start)
	visited = []

	# While elements are in the stack (unexplored nodes exists)
	while stack:
		
		# Pop the top of the stack
		node = stack.pop()
		if node is end:
			visited.append(node)
			return visited
		
		# Only add white nodes
		if node not in visited:
			visited.append(node)
	
			# Add child nodes to stack
			if successorsf(node):
				for child_node in successorsf(node):
					stack.append(child_node)
			else:
				visited.remove(node)

	return visited

		
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
	print(depthFirstSearch('a', 'm', successorsf))