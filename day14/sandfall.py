''' sand is falling an need to know where it goes '''

# writing the parameters here, could also just call from command line
filename = 'input_day14.data'
testfile = 'test_day14.data'


# pull in the rock map and break it out
def file_input(filename = 'input_day14.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		rocklines = infile.read().splitlines()

	return rocklines


def process_commands(rocklines):
	''' process the rock inputs into a list of rocks formation '''

	# one line per formation
	# formation is a list of tuple pairs
	# formation = [((x,y),(x1,y1))]
	formations = []
	for line in rocklines:
		formation = []
		for position_string in line.split(' -> '):
			string_list = position_string.split(',')
			position_tuple = (int(string_list[0]), int(string_list[1]))
			formation.append(position_tuple)
		formations.append(formation)
	return formations


def build_grid(formations):
	''' create a grid of the rocks '''
	# grid nodes have values
	# 0 - abyss
	# 1 - air
	# 2 - rock
	# 3 - sand

	# determine min and max x
	# determin max y
	# x_min -1 is abyss	
	x_max = 0
	y_max = 0
	x_min = 100000
	y_min = 0
	for formation in formations:
		for coordinate in formation:
			if coordinate[0] > x_max:
				x_max = coordinate[0]
			if coordinate[0] < x_min:
				x_min = coordinate[0]
			if coordinate[1] > y_max:
				y_max = coordinate[1]
	# build grid of air and mark the abyss on left edge
	rock_grid = {}
	for y in range(y_min, y_max + 1):
		rock_grid[(x_min-1,y)] = 0
		for x in range(x_min, x_max + 1):
			rock_grid[(x,y)] = 1		

	return rock_grid


def add_formation(rock_grid, formation):
	''' given a single formation list, add it to the grid '''
	for move in formation:
		print("something")
		#do something
	return


def move_sand(current_coord, rock_grid):
	''' determine where the sand will go next or stop '''
	next_down = (current_coord[0], current_coord[1] - 1)
	if rock_grid[next_down] > 1:
		# can't go there, check 
		next_right = (current_coord[0] + 1, current_coord[1] - 1)
		if rock_grid[next_right] >1:
			# can't go down to right
			next_left = (current_coord[0] - 1, current_coord[1] - 1)
			if rock_grid[next_left] > 1:
				# can't go there
				return current_coord
			else:
				# abyss or air
				return next_left



	return next_coord



def drop_sand(rock_grid):
	''' start dropping sand and track what happens stop at abyss '''
	sand_start = (500,0)
	total_moves = 0
	current_coord = sand_start
	abyss = False
	
	# now start dropping from start location
	while abyss == False:
		sand_movng = True
		total_moves += 1
		while sand_movng == True:
			next_coord = move_sand(current_coord, rock_grid)
			if next_coord == current_coord:
				print("sand has stopped")
				current_coord = sand_start
				sand_movng = False
			elif next_coord[0] == -1:
				print("into the abyss")
				abyss = True
			else:
				current_coord = next_coord

	return total_moves




