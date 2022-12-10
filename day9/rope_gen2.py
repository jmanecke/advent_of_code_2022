''' second generation rope object that does it better than gen 1 '''

# dict of four lists: [command, neumonic, tuple]
cartesian_moves = {
	"L": ['Left', 'x-', (-1,0)],
	"R": ['Right', 'x+', (1,0)],
	"D": ['Down', 'y-', (0,-1)],
	"U": ['Up', 'y+', (0,1)]
}


### use a rope class and a knot class
class RopeGen2:
	''' rope with a configurable number of knots that moves and tracks where its tail goes '''

	def __init__(self, number_knots):
		'''ropes start at 0, 0 and have configurable number or knots'''
		self.number_knots = number_knots
		self.x_coords = []
		self.y_coords = []
		self.tail_history = set()
		# every knot starts at 0,0 so put them there
		for i in range(0,number_knots):
			self.x_coords[i] = 0
			self.y_coords[i] = 0
		self.tail_history.add((0,0))
		# create a transform tuple for each move

		return

	def move_command(vector):
		''' takes vector a makes single head moves to get there '''
		move_tuple = cartesian_moves[vector[0]]
		magnitude = vector[1]
		for i in range(0,magnitude):
			self.move_rope(move_tuple)
		return


class Knot:
	''' knot in a rope '''

	def _init__(self, parent_knot = "HEAD"):
		'''start at 0,0 and have parent unless head'''
		self.x_coord = 0
		self.y_coord = 0
		self.parent = parent_knot
		return


	def follow_parent(self):
		'''check where parent is and move if required'''
		knot_coord = (self.x_coord,self.y_coord)
		parent_coord = (self.parent.x_coord,self.parent.y_coord)
		move_transform = self.find_move(knot_coord, parent_coord)
		self.x_coord += move_transform[0]
		self.y_coord += move_transform[1]
		return


#### better functions
def find_move(knot_coord, parent_coord):
	'''given coordinates of a knot and its parent return a move tuple'''
	move_tuple = (0,0)
	return move_tuple