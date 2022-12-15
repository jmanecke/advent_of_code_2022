'''given a grid of tree heights, find ones that are taller than others on path to edge'''

# assumption
# tree heights are single digit integers and arranged in a rectangular grid

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


def give_answer():
	''' just run this to spit out an answer '''
	mytrees = file_input()
	print("The number of trees visible is: {}".format(mytrees.trees_visible()))
	print("The highest scenic score is: {}".format(mytrees.trees_scenic()))
	return


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
		#if either value is outside paraters show error message
		if row < self.row_total and column < self.column_total:
			arraypos = self.row_total * row + column
			treevalue = self.gridarray[arraypos]
			return treevalue, arraypos
		else:
			return "Error the grid is " + str(self.row_total) + " rows x " + str(self.column_total) + " columns"


	def getrow(self, row):
		'''given a row index return the row list'''
		if row < self.row_total:
			treerow = []
			for i in range(0, self.column_total):
				treerow.append(self.gettree(row, i)[0])
			return treerow
		else:
			return "Error the grid is " + str(self.row_total) + " rows"


	def getcolumn(self, column):
		'''given a column index return the column list'''
		if column < self.column_total:
			treecolumn = []
			for i in range(0, self.column_total):
				treecolumn.append(self.gettree(i, column)[0])
			return treecolumn
		else:
			return "Error the grid is " + str(self.column_total) + " columns"


	def trees_visible(self):
		'''calculates number of trees trees_visible from viewpoint'''
		# arraypos is the unique tree identifier
		visible_set = set()
		# add edge rows and columns first only for visible
		for i in range(0, self.column_total):
			visible_set.add(i)
			visible_set.add(i+(self.row_total - 1) * self.column_total)
		for i in range(1, self.row_total - 1):
			visible_set.add(i * self.column_total)
			visible_set.add((i+1) * self.column_total-1)

		# now go through interior trees
		# first by row
		for i in range(1,self.row_total-1):
			row = self.getrow(i)
			# go across a row
			for j in range(1, self.column_total-1):
				#look left
				if row[j] > max(row[:j]):
					visible_set.add(self.gettree(i,j)[1])
				#look right
				if row[j] > max(row[j+1:]):
					visible_set.add(self.gettree(i,j)[1])


		# next by columns
		for i in range(1,self.column_total-1):
			column = self.getcolumn(i)
			# go down a column
			for j in range(1, self.row_total-1):
				#look up
				if column[j] > max(column[:j]):
					visible_set.add(self.gettree(j,i)[1])
				#look right
				if column[j] > max(column[j+1:]):
					visible_set.add(self.gettree(j,i)[1])

		visible_number = len(visible_set)
		return visible_number


	def trees_scenic(self):
		'''calculates number of trees trees_visible from viewpoint'''
		# arraypos is the unique tree identifier
		number_trees = self.row_total * self.column_total
		highest_score = 0
		# go through each tree even throug we know edge trees return zero
		# could do small optimization by only checking interior trees
		for tree_pos in range(0,number_trees):
			tree_score = self.calc_scenic_score(tree_pos)
			if tree_score > highest_score:
				highest_score = tree_score

		return highest_score


	def calc_scenic_score(self,arraypos):
		'''given a tree array position calculate it's scenic score'''
		treerow_number = int(arraypos/self.column_total)
		treecolumn_number = arraypos - treerow_number * self.column_total
		# get back the trees row and column
		treerow = self.getrow(treerow_number)
		treecolumn = self.getcolumn(treecolumn_number)
		tree_height = self.gettree(treerow_number, treecolumn_number)[0]
		upscore = 0
		downscore = 0
		leftscore = 0
		rightscore =0
		# look up
		if treerow_number != 0:
			up_potential = treecolumn[:treerow_number]
			up_potential.reverse()
			done = 0
			for nextree in up_potential:
				if nextree < tree_height and done !=1:
					upscore += 1
				elif done != 1:
					upscore += 1
					done = 1
		# look down
		if treerow_number + 1 != self.row_total:
			down_potential = treecolumn[treerow_number+1:]
			done = 0
			for nextree in down_potential:
				if nextree < tree_height and done !=1:
					downscore += 1
				elif done != 1:
					downscore += 1
					done = 1

		# look left
		if treecolumn_number != 0:
			left_potential = treerow[:treecolumn_number]
			left_potential.reverse()
			done = 0
			for nextree in left_potential:
				if nextree < tree_height and done !=1:
					leftscore += 1
				elif done != 1:
					leftscore += 1
					done = 1

		# look right
		if treecolumn_number + 1 != self.column_total:
			right_potential = treerow[treecolumn_number+1:]
			done = 0
			for nextree in right_potential:
				if nextree < tree_height and done !=1:
					rightscore += 1
				elif done != 1:
					rightscore += 1
					done = 1

		tree_score = upscore * downscore * leftscore * rightscore
		return tree_score