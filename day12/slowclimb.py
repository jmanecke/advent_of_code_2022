''' need to slowly cliimb up to get better signal '''

# writing the parameters here, could also just call from command line
filename = 'input_day12.data'
testfile = 'test_day12.data'

# read in grid by lines
def file_input(filename = 'input_day12.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		grid_lines = infile.read().splitlines()
	return grid_lines


class Grid:
	'''grid of elevations with start and end'''
	def __init__(self):
		self.matrix = []
		self.total_nodes = 0

	def build_grid(self, grid_lines):
		'''convert the lines into a nxn matrix with integer values on nodes'''
		row_number = 0
		number_columns = len(grid_lines[0])
		for row in grid_lines:
			if len(row) != number_columns:
				print("Grid rows different lenghts, data error")
				return
			rowlist = []
			rowcharlist = [*row]
			column = 0
			for character in rowcharlist:
				if character == 'S':
					start_pos = (column, row_number)
					character = 'a'
				if character == 'E':
					end_pos = (column, row_number)
					character = 'z'
				rowlist.append(ord(character) - 97)
				column += 1
			self.matrix.append(rowlist)
			row_number += 1
		self.total_nodes = row_number * number_columns
		self.start_node = self.find_node(start_pos[0], start_pos[1])
		self.goal_node = self.find_node(end_pos[0], end_pos[1])
		return


	def find_node(self,xcoord, ycoord):
		'''given x y in grid return node node_number'''
		return xcoord + ycoord * len(self.matrix[0])


	def elevation(self, x, y):
		''' give an x and y get back the elevation of that node '''
		return self.matrix[y][x]

	def a_nodes(self):
		'''find nodes that are 0 elevation'''
		a_nodes = []
		for y in range(0, len(self.matrix)):
			for x in range(0,len(self.matrix[0])):
				if self.matrix[y][x] == 0:
					a_nodes.append(self.find_node(x,y))
		return a_nodes



class Graph:
	''' graph of adjacencies that can BFS search itself'''
	def __init__(self):
		self.graph = {}
		return


	def add_edge(self, node_1, node_2):
		'''add an edge to the graph'''
		if node_1 not in self.graph:
			self.graph[node_1] = []
		self.graph[node_1].append(node_2)
		return


	def bfs_find_path(self,start_node, goal_node):
		'''finds the shortest path and builds the path then returns it'''
		#mark all nodes as not visited
		total_nodes = max(self.graph) +1
		print("Total visitable nodes is: {}".format(total_nodes))
		visited = [False] * total_nodes

		# mark start node visited and add to the queue
		# queue is a list of paths we're following
		queue = []
		queue.append([start_node])
		visited[start_node] = True

		# pull from queue and mark visited if not there before, add adjacent to queue
		while queue:
			# deque path and work with last node
			path = queue.pop(0)
			if len(path) > 12:
				print("popped at {} long path".format(path))
			#print(path)
			# get adjacent to last node and go through each neighbor
			last_node_neigbors = self.graph[path[-1]]
			for neighbor in last_node_neigbors:
				new_path = list(path)
				queue.append(new_path)
				# check if we're at the goal
				if neighbor == goal_node:
					print("Shortest path = ", new_path)
					print("length of path: {}".format(len(new_path)))
					return
				# updated visited and put path back into queue if not repeating
				if visited[neighbor] == False:
					queue.append(new_path)
					visited[neighbor] = True
		print("reached end with no path found")
		return


	def bfs_find_steps(self,start_node, goal_node):
		'''finds only the number of steps in the shortest path'''
		#mark all nodes as not visited
		total_nodes = max(self.graph) +1
		print("Total visitable nodes is: {}".format(total_nodes))
		visited = [False] * total_nodes

		# mark start node visited and add to the queue
		# queue is a list of nodes and steps to them we're checking
		steps = 0
		queue = []
		queue.append((start_node, steps))
		visited[start_node] = True

		# pull from queue and mark visited if not there before, add adjacent to queue
		while queue:
			# deque a vertex to check adjacents
			path = queue.pop(0)
			#print(path)
			# get adjacent to last node and go through each neighbor
			last_node_neigbors = self.graph[path[0]]
			nextstep = path[1] + 1
			for neighbor in last_node_neigbors:
				
				# check if we're at the goal
				if neighbor == goal_node:
					print("Shortest path found")
					print("length of path: {}".format(nextstep))
					return
				# updated visited and put path back into queue if not repeating
				if visited[neighbor] == False:
					queue.append(((neighbor,nextstep)))
					visited[neighbor] = True
		print("reached end with no path found")
		return


def find_adjacencies(grid, graph):
	'''go around the grid and evaluate moves adding to graph'''
	grid_rows = len(grid.matrix)
	grid_colmns = int(grid.total_nodes / grid_rows)

	for y in range(0, grid_rows):
		print("y {}".format(y))
		for x in range(0, grid_colmns):
			print("  x {}".format(x))
			n1 = grid.find_node(x,y)
			if x != 0:
				# check left
				if grid.elevation(x,y) +1  >= grid.elevation(x-1,y):
					n2 = grid.find_node(x-1,y)
					graph.add_edge(n1, n2)

			if x != grid_colmns -1:
				# check right
				if grid.elevation(x,y) +1 >= grid.elevation(x+1,y):
					n2 = grid.find_node(x+1,y)
					graph.add_edge(n1, n2)

	for x in range(0, grid_colmns):
		print("x {}".format(x))
		for y in range(0, grid_rows):
			print("  y {}".format(y))
			n1 = grid.find_node(x,y)
			if y != 0:
				# check up
				if grid.elevation(x,y) + 1 >= grid.elevation(x,y-1):
					n2 = grid.find_node(x,y-1)
					graph.add_edge(n1, n2)

			if y != grid_rows -1:
				# check down
				if grid.elevation(x,y) + 1  >= grid.elevation(x,y+1):
					n2 = grid.find_node(x,y+1)
					graph.add_edge(n1, n2)
	return


def give_answer(fileinput = 'input_day12.data'):
	grid_lines = file_input(fileinput)
	mygrid = Grid()
	mygrid.build_grid(grid_lines)
	mygraph = Graph()
	find_adjacencies(mygrid, mygraph)
	mygraph.bfs_find_steps(mygrid.start_node, mygrid.goal_node)

def part2_answer(fileinput = 'input_day12.data'):
    ''' figure out multiple points'''
    # build list of starting points
    grid_lines = file_input(fileinput)
    mygrid = Grid()
    mygrid.build_grid(grid_lines)
    mygraph = Graph()
    find_adjacencies(mygrid, mygraph)
    a_nodes = mygrid.a_nodes()
    for node in a_nodes:
    	mygraph.bfs_find_steps(node, mygrid.goal_node)
