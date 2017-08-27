# Josh Mau
# BFS and DFS implementation in python
# August 26th, 2017

from copy import copy

def breadthFirstSearch(start, end, successorsf, visited=[], queue=[], path=[]):
	pass
		
	
def depthFirstSearch(start, end, successorsf, visited=[], path=[]):
	path.append(start)
	
	if start is end:
		return path
	
	else:
		if successorsf(start):
			for child in successorsf(start):
				if child not in visited:
					visited.append(child)
					current_path = depthFirstSearch(child, end, successorsf, visited, path)
					if current_path:
						return current_path
					else:
						path.pop()
	return None

	
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