''' second generation rope object that does it better than gen 1 '''

# pull from coordinate math, create the coordinate transform for each move
# break each "move" input into single steps of one move
# a knot can only do one of these moves each step

# two dict of four lists: [command, neumonic, tuple]
cartesian_moves = {
	"L": ['Left', 'x-', (-1,0)],
	"R": ['Right', 'x+', (1,0)],
	"D": ['Down', 'y-', (0,-1)],
	"U": ['Up', 'y+', (0,1)]
}

# not used but leaving here as it helps understanding
diagnonal_moves = {
	"UR": ['UpRight',   'x+y+', ( 1, 1)],
	"UL": ['UpLeft',    'x-y+', (-1, 1)],
	"DR": ['DownRight', 'x+y-', ( 1,-1)],
	"DL": ['DownLeft',  'x-y-', (-1,-1)]
}

# writing the parameters here, could also just call from command line
filename = 'input_day9.data'
testfile = 'test_day9.data'
test2file = 'test2_day9.data'


# pull in the moves and put them into an array of move vecotors
def file_input(filename = 'input_day9.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		movevectors = infile.read().splitlines()

	# make a list of move tuples
	ropemoves = []
	for move in movevectors:
		themove = move.split()
		movenumber = int(themove[1])
		ropemoves.append((themove[0], movenumber))

	return ropemoves


### use a rope class and a knot class
# rope is made up of two or more knots, must have a head knot, last knot is tail

class RopeGen2:
	''' rope with a configurable number of knots that moves and tracks where its tail goes '''

	def __init__(self, number_knots):
		'''ropes start at with all knots at 0, 0 and have configurable number of knots'''
		self.number_knots = number_knots
		self.tailnumber = number_knots -1
		self.tail_history = set()
		self.tail_history.add((0,0))
		# add knots to the rope
		self.myknots = [(Knot("HEAD"),"head")]
		lastadded = self.myknots[0]
		# set it as head
		lastadded[0].is_head = True
		for i in range(1,number_knots):
			self.myknots.append((Knot(lastadded[0]),i))
			lastadded = self.myknots[-1]
		return

	def move_command(self, vector):
		''' takes vector move and breaks into into one or more single head moves to get there '''
		move_tuple = cartesian_moves[vector[0]][2]
		magnitude = vector[1]
		for i in range(0,magnitude):
			self.move_rope(move_tuple)
		return


	def move_rope(self, move_tuple):
		'''move the rope one head positon then update all knots'''
		# first move the head
		self.myknots[0][0].move_knot(move_tuple)
		# go through each knot 
		for i in range(1,self.number_knots):
			self.myknots[i][0].follow_parent()
		# update tail position
		self.tail_history.add(self.myknots[-1][0].coordinates())


	def knot_positions(self):
		'''output the positions of all knots in the rope'''
		for knot in self.myknots:
			print("Name: {} coords: {}".format(knot[1],knot[0].coordinates()))
		return


# knots have a partent knot which is above them unless they are the head, knots move only based on their parent
class Knot:
	''' knot in a rope '''

	def __init__(self, parent_knot = "HEAD"):
		'''start at 0,0 and have parent unless head'''
		self.x_coord = 0
		self.y_coord = 0
		self.is_head = False
		self.parent = parent_knot
		return


	def follow_parent(self):
		'''check where parent is and make one move if required'''
		knot_coord = (self.x_coord,self.y_coord)
		parent_coord = (self.parent.x_coord,self.parent.y_coord)
		if ismove_required(knot_coord, parent_coord):
			move_transform = find_move(knot_coord, parent_coord)
			self.x_coord += move_transform[0]
			self.y_coord += move_transform[1]
		return


	def coordinates(self):
		'''return the current coordinates as a tuple'''
		my_location = (self.x_coord, self.y_coord)
		return my_location


	def move_knot(self, move_tuple):
		''' move a knot by applying the move tuple '''
		self.x_coord += move_tuple[0]
		self.y_coord += move_tuple[1]
		my_location = (self.x_coord, self.y_coord)
		return my_location


#### better functions
def find_move(knot_coord, parent_coord):
	'''given coordinates of a knot and its parent select and return a move tuple'''
	params = find_parameters(knot_coord, parent_coord)
	if params[2] or params[3]:
		# horizontal or vertical move
		if params[2] and knot_coord[0] > parent_coord[0]:
			# horizontal move left
			move_tuple = cartesian_moves['L'][2]
		elif params[2] and knot_coord[0] < parent_coord[0]:
			# horizontal move right
			move_tuple = cartesian_moves['R'][2]
		elif params[3] and knot_coord[1] > parent_coord[1]:
			# vertical move down
			move_tuple = cartesian_moves['D'][2]
		elif params[3] and knot_coord[1] < parent_coord[1]:
			# vertical move down
			move_tuple = cartesian_moves['U'][2]
		else:
			print("Something went wrong")
	else:
		#diagnonal_move
		if params[0] == 2 and params [1] == 2:
			# following a diagonal parent diagonal move
			x_change = int((parent_coord[0] - knot_coord[0])/2)
			y_change = int((parent_coord[1] - knot_coord[1])/2)
		elif params[0] == 2:
			# half x distance move, full y distance move
			x_change = int((parent_coord[0] - knot_coord[0])/2)
			y_change = parent_coord[1] - knot_coord[1]
		elif params[1] == 2:
			# full x distance move, half y distance move
			x_change = parent_coord[0] - knot_coord[0]
			y_change = int((parent_coord[1] - knot_coord[1])/2)
		else:
			print("Something went wrong")
		move_tuple = (x_change, y_change)
	return move_tuple

def ismove_required(knot_coord, parent_coord):
	''' check if they are one away '''
	xsquare = abs(parent_coord[0] - knot_coord[0])**2
	ysqare = abs(parent_coord[1] - knot_coord[1])**2
	distance_squared = xsquare + ysqare
	if distance_squared > 2:
		return True
	else:
		return False

def find_parameters(knot_coord, parent_coord):
	'''evaluates both postions and breaks out find_parameters'''
	# returns a four position tuple (0, 1, 2, 3)
	#  0 - integer - x distance 
	#  1 - integer - y distance
	#  2 - boolean - knots horizontally aligned?
	#  3 - boolean - knots vertically aligned?
	#
	x_distance = abs(parent_coord[0] - knot_coord[0])
	y_distance = abs(parent_coord[1] - knot_coord[1])
	vert_aligned = (parent_coord[0] == knot_coord[0])
	horiz_aligned = (parent_coord[1] == knot_coord[1])
	paramter_tuple = (x_distance, y_distance, horiz_aligned, vert_aligned)
	return paramter_tuple


def give_answer():
	''' just run this to spit out an answer '''
	ropemoves = file_input()
	part1_rope = RopeGen2(2)
	part2_rope = RopeGen2(10)
	# run both ropes through the commands
	for move in ropemoves:
		part1_rope.move_command(move)
		part2_rope.move_command(move)
	print("The part 1 tail has been to {} different positions".format(len(part1_rope.tail_history)))
	print("The part 2 tail has been to {} different positions".format(len(part2_rope.tail_history)))