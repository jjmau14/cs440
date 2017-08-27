from copy import copy

def breadthFirstSearch(start, end, successorsf, visited=[], queue=[], parentTree={}):
	queue.append(start)
	
	while queue:
		node = queue.pop()
		visited.append(node)
		
		if node is end:
			return getTree(parentTree, start, end)
		
		if successorsf(node):
			for child in successorsf(node):
				queue.insert(0, child)
				parentTree[child] = node
				
def getTree(parents, start, end, path=[]):
	curr = end
	while curr != start:
		path.insert(0, curr)
		curr = parents[curr]
	path.insert(0,curr)
	return path
	
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
	print(breadthFirstSearch('a', 'z', successorsf))