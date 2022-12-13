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
					self.start_pos = (row_number,column)
					character = 'a'
				if character == 'E':
					self.end_pos = (row_number,column)
					character = 'z'
				rowlist.append(ord(character) - 97)
				column += 1
			self.matrix.append(rowlist)
			row_number += 1
		self.total_nodes = row_number * number_columns
		return


	def find_node(self,xcoord, ycoord):
		'''given x y in grid return node node_number'''
		return xcoord + ycoord * len(self.matrix[0])


	def elevation(self, x, y):
		''' give an x and y get back the elevation of that node '''
		return self.matrix[y][x]


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


	def bfs_search(self,start_node):
		#mark all nodes as not visited
		total_nodes = max(self.graph) +1
		print("total_nodes is: {}".format(total_nodes))
		visited = [False] * total_nodes

		# mark start node visited and add to the queue
		queue = []
		queue.append(start_node)
		print("node {} put in queue".format(start_node))
		visited[start_node] = True

		# pull from queue and mark visited if not there before, add adjacent to queue
		while queue:
			# deque vertex
			vertex = queue.pop(0)
			print(vertex, end = " ")
			# get adjacent and check if visited
			for i in self.graph[vertex]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


def find_adjacencies(grid, graph):
	'''go around the grid and evaluate moves adding to graph'''
	grid_rows = len(grid.matrix)
	grid_colmns = int(grid.total_nodes / grid_rows)

	for y in range(0, grid_rows):
		print("y {}".format(y))
		for x in range(0, grid_colmns):
			print("  x {}".format(x))
			n1 = x + y * grid_rows
			if x != 0:
				# check left
				if grid.elevation(x,y) <= 1+ grid.elevation(x-1,y):
					n2 = (x-1) * y * grid_rows
					graph.add_edge(n1, n2)

			if x != grid_colmns -1:
				# check right
				if grid.elevation(x,y) <= 1 + grid.elevation(x+1,y):
					n2 = (x+1) + y * grid_rows
					graph.add_edge(n1, n2)

	for x in range(0, grid_colmns):
		print("x {}".format(x))
		for y in range(0, grid_rows):
			print("  y {}".format(y))
			n1 = x + y * grid_rows
			if y != 0:
				# check up
				if grid.elevation(x,y) <= 1 + grid.elevation(x,y-1):
					n2 = x + (y+1) * grid_rows
					graph.add_edge(n1, n2)

			if y != grid_rows -1:
				# check down
				if grid.elevation(x,y) <= 1 + grid.elevation(x,y+1):
					n2 = x + (y+1) * grid_rows
					graph.add_edge(n1, n2)
	return


def give_answer():
	grid_lines = file_input(slowclimb.testfile)
	mygrid = slowclimb.Grid()
	mygrid.build_grid(grid_lines)
	mygraph = slowclimb.Graph()
	find_adjacencies(mygrid, mygraph)
	mygraph.bfs_search(mygrid.start_pos)


