def dfs(dict, start):
	stack, path = [start], []

	while stack:
		vertex = stack.pop()
		if vertex in path:
			continue
		path.append(vertex)
		for nbr in graph[vertex]:
			stack.append(nbr)
	return path
	
def bfs(dict, start):

	queue, path = [start], []
	levels = {start: 0}
	
	while queue:
		vertex = queue.pop(0)
		if vertex in path:
			continue
		path.append(vertex)
		for nbr in graph[vertex]:
			queue.append(nbr)
			if nbr not in levels:
				levels[nbr] = levels[vertex] + 1 
	return path, levels

graph = {}

graph[0] = [1,5]
graph[1] = [2]
graph[2] = [3]
graph[3] = [4,5]
graph[4] = [0]
graph[5] = [2,4]

print(bfs(graph, 0))
