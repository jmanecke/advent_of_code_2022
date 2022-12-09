'''given a grid of rope move figure out where the tail goes'''

# assumption

import array

# writing the parameters here, could also just call from command line
filename = 'input_day9.data'
testfile = 'test_day9.data'

# pull in the tree grid and put into an array
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


# start at a 0,0 position, coordinates are positive or negative integers

# head position and tail position - maintain two coordinate pairs

# at the end of each move, write tail coordinates to a set (at at the 0,0 start) - part 1 answer is length

# followin things happen over and over again (these are my functions):
#   move_head - given a move vector (direciton and magntiude) determine the new head loacation
#	tail_chase - given head position tail position, determine where the tail goes
#	update_hisotry - convert tail coordinate list to a tuple (hashable) and add is to the set

head_coordinates = [0,0]
tail_coordinates = [0,0]
tail_history = set()

def makemoves(ropemoves):
	'''runs through the moves updating the tail history along the way'''
	update_tail_history()
	for vector in ropemoves:
		head_coordinates = move_head(vector)
		newtail = tail_chase()
		update_tail_history()
	return


def give_answer():
	''' just run this to spit out an answer '''
	ropemoves = file_input()
	makemoves(ropemoves)
	print("The tail has been to {} different positions".format(len(tail_history)))


def move_head(vector):
	''' moves the head based on what the vector move is '''
	if vector[0] == 'L':
		head_coordinates[0] += -1 * vector[1]
	elif vector[0] == 'R':
		head_coordinates[0] += vector[1]
	elif vector[0] == 'U':
		head_coordinates[1] += vector[1]
	elif vector[0] == 'D':
		head_coordinates[1] += -1 * vector[1]
	else:
		print("bad vector direction in move, skipping")

	return


def tail_chase():
	'''based on head and tail position, determine the appropriate tail move and make it'''
	# figure move type to start
	if head_coordinates == tail_coordinates:
		# head on tail no move takes place
		return
	else:
		if head_coordinates[0] == tail_coordinates[0]:
			# same x coordinate so move in y if more and one greater
			if abs(head_coordinates[1] == tail_coordinates[1]) == 1:
				# only one away so no move
				return
				if head_coordinates[1] > tail_coordinates[1]:
					# tail moves up to one below head
					tail_coordinates[1] = head_coordinates[1] -1
				else:
					# tail moves down to one above head
					tail_coordinates[1] = head_coordinates[1] +1

		elif head_coordinates[1] == tail_coordinates[1]:
			# same y coordinate so move in x if more and one greater
			if abs(head_coordinates[0] == tail_coordinates[0]) == 1:
				# only one away so no move
				return
				if head_coordinates[0] > tail_coordinates[0]:
					# tail moves right to one left of head
					tail_coordinates[0] = head_coordinates[0] -1
				else:
					# tail moves left to one right of head
					tail_coordinates[0] = head_coordinates[0] +1

		else:
			# diagonal move
			x = 1

	return


def update_tail_history():
	'''add the tail position to the history set in a hashable way'''
	history_tuple = (tail_coordinates[0], tail_coordinates[1])
	tail_history.add(history_tuple)
	return
