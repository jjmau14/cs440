# Josh Mau
# BFS and DFS implementation in python
# August 26th, 2017

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
		
	
def depthFirstSearch(startState, goalState, successorsf):
	dfs = []
	stack = list(startState)
	
	while stack:
		node = stack.pop()
		if not node in dfs:
			dfs.append(node)
			if successorsf(node):
				for child in successorsf(node):
					stack.append(child)
	return dfs
	
	
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
	print(breadthFirstSearch('a', 'm', successorsf))
