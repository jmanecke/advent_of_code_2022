'''given a grid of tree heights, find ones that are taller than others on path to edge'''

# assumption
# tree heights are single digit integers and arranged in a rectangular grid
# support treegrids up to 999 x 999

import array

# writing the parameters here, could also just call from command line
filename = 'input_day8.data'
testfile = 'test_day8.data'

# pull in the tree grid and put into an array
def file_input(filename = 'input_day8.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		gridlines = infile.read().splitlines()

	# first line is data and width is constant
	trees_across = len(gridlines[0])
	mytrees = TreeGrid(trees_across)
	for rowstring in gridlines:
		row_heights = []
		for height in rowstring:
			row_heights.append(int(height))
		mytrees.addrow(row_heights)

	return mytrees


class TreeGrid:
	'''quick and dirty 2d array for the grid of trees'''

	def __init__(self, vertical_colmns):
		'''just need to know who many coloumns to start it off then append rows'''
		self.column_total = vertical_colmns
		self.row_total = 0
		self.gridarray = array.array("I",[])
		return


	def addrow(self, row_list):
		'''add another row of integer tree heights'''
		if len(row_list) != self.column_total:
			# bad row
			print("tried to append a row that was {} trees long".format(len(row_list)))
			print("this grid is for {} long rows".format(self.column_total))
		else:
			self.gridarray.extend(row_list)
			self.row_total += 1
		return

	def gettree(self, row, column):
		'''given row and colmn index reutrn the tree height value'''
		arraypos = self.column_total * column + row
		treevalue = self.gridarray[arraypos]
		return treevalue

	def trees_visible(self):
		'''calculates number of trees trees_visible from viewpoint'''
		# arraypos is the unique tree identifier
		visible_set = set()
		# add edge rows and columns first
		for i in range(0, self.column_total):
			visible_set.add(i)
			visible_set.add(i+(self.row_total - 1) * self.column_total)
		for i in range(1, self.row_total - 1):
			visible_set.add(i * self.column_total)
			visible_set.add((i+1) * self.column_total -1)

		# now go through interior trees
		

		return visible_set








