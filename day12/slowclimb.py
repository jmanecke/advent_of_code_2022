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





def find_adjacency(grid_matrix, node_number):
	'''given a node find which ways you can go'''


class Grid:

	def __init__(self):
		self.matrix = []
		self.number_rows = 0
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
			self.number_rows += 1
		self.total_nodes = row_number * number_columns
		return


		def find_node(self,xcoord, ycoord):
			'''given x y in grid return node node_number'''
			return xcoord + ycoord * self.number_rows


		def node_info(self, node_number): 
			''' given a node provide info '''
			elevation = 

			return elevation, coordinates, adjacency_list




