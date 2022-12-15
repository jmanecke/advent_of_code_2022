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
# need to add coordinates for all the places the tail has been

# following things happen over and over again (these are my functions):
#   move_head - given a move vector (direciton and magntiude) determine the new head loacation
#	tail_chase - given head position and tail position, determine where the tail goes and trace each place it hits
#		diagonal_move - one step move so next move is an up/down left/right
#		updown_move - one or more moves in y
#		leftright_move - on or more moves in x
#	update_hisotry - convert tail coordinate list to a tuple (hashable) and add is to the set

head_coordinates = [0,0]
tail_coordinates = [0,0]
tail_history = set()


def makemoves(ropemoves):
	'''runs through the moves updating the tail history along the way'''
	update_tail_history()
	for vector in ropemoves:
		move_head(vector)
		newtail = tail_chase()
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
	'''based on head and tail position, determine the appropriate tail moves and make them'''
	# figure move type to start
	x_distance = abs(head_coordinates[0] - tail_coordinates[0])
	y_distance = abs(head_coordinates[1] - tail_coordinates[1])
	vert_aligned = (head_coordinates[0] == tail_coordinates[0])
	horiz_aligned = (head_coordinates[1] == tail_coordinates[1])


	if head_coordinates == tail_coordinates:
		# head on tail no move takes place
		return
	elif x_distance == 1 and y_distance ==1:
		# one away diagonally no move takes place
		return
	elif head_coordinates[0] == tail_coordinates[0] and x_distance == 1:
		# one above or below no move takes place
		return
	elif head_coordinates[1] == tail_coordinates[1] and y_distance == 1:
		# one left or right no move takes place
		return
	elif not vert_aligned and not horiz_aligned and (x_distance != 1 or y_distance != 1):
		#diagonal move required first
		diagonal_move(x_distance, y_distance)
		x_distance = abs(head_coordinates[1] - tail_coordinates[1])
		y_distance = abs(head_coordinates[0] - tail_coordinates[0])

	# check if we still need more moves if not then return
	if not (x_distance > 1 or y_distance > 1):
		# 
		return

	# if we're here then up/down or left/right moves of 1 or move spaces remain
	if head_coordinates[0] == tail_coordinates[0]:
		# up / down move
		updown_move()
	elif head_coordinates[1] == tail_coordinates[1]:
		# left right move
		leftright_move()
	else:
		print("something went wrong")
	return


def updown_move():
	'''moves up or down to get within one and updates trace'''
	common_x = head_coordinates[0]
	# same x coordinate so move in y if more and one greater
	if head_coordinates[1] > tail_coordinates[1]:
		# tail moves up to one below head
		starting_y = tail_coordinates[1]
		ending_y = head_coordinates[1] -1
		tail_coordinates[1] = ending_y
		for y in range(starting_y, ending_y+1):
			tail_history.add((common_x,y))
	else:
		# tail moves down to one above head
		starting_y = tail_coordinates[1]
		ending_y = head_coordinates[1] +1
		tail_coordinates[1] = ending_y
		for y in range(ending_y,starting_y +1):
			tail_history.add((common_x,y))
	return


def leftright_move():
	'''moves left or right to get within one and updates trace'''
	common_y = head_coordinates[1]
	if head_coordinates[0] > tail_coordinates[0]:
		# tail moves right to one left of head
		starting_x = tail_coordinates[0]
		ending_x = head_coordinates[0] -1
		tail_coordinates[0] = ending_x
		for x in range(starting_x, ending_x +1):
			tail_history.add((x,common_y))
	else:
		# tail moves left to one right of head
		starting_x = tail_coordinates[0]
		ending_x = head_coordinates[0] +1					
		tail_coordinates[0] = ending_x
		for x in range(ending_x,starting_x +1):
			tail_history.add((x,common_y))
	return


def diagonal_move(x_distance, y_distance):
	'''make one diagonal move and update tail_history'''
	if x_distance > y_distance:
		# need to move vertical one then horizontally
		# first move to same vertical coordinate as head
		tail_coordinates[1] = head_coordinates[1]
		if head_coordinates[0] > tail_coordinates[0]:
			#head is to the right of tail
			tail_coordinates[0] += 1
		else:
			# tail is to the right of head
			tail_coordinates[0] += -1

	elif y_distance > x_distance:
		# need to move horizontally one then vertically
		# first move to same horizontal coordinate as head
		tail_coordinates[0] = head_coordinates[0]		
		if head_coordinates[1] > tail_coordinates[1]:
			#head is above tail
			tail_coordinates[1] += 1
		else:
			# tail is above head
			tail_coordinates[1] += -1

	update_tail_history()
	return


def update_tail_history():
	'''add the tail position to the history set in a hashable way'''
	history_tuple = (tail_coordinates[0], tail_coordinates[1])
	tail_history.add(history_tuple)
	return
