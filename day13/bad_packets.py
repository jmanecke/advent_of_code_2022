'''packets are out of order so need to parse the input and figure out which ones are no good'''

# writing the parameters here, could also just call from command line
filename = 'input_day13.data'
testfile = 'test_day13.data'


# pull in the raw packet ros and put them into an array of packet lines
def file_input(filename = 'input_day13.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		packetlines = infile.read().splitlines()
	thepackets = {}
	for i in range (2,len(packetlines),3):
		if len(packetlines[i]) != 0:
			print("bad data")
		else:
			packetcontents = {"left": eval(packetlines[i-2]), "right": eval(packetlines[i-1])}
			thepackets[int((i+1)/3)]=packetcontents
	return thepackets


def eval_packet_pairs(thepackets):
	''' go through the pairs of packet and check if they are in the right order '''
	indices_sum = 0
	for i in range(1,len(thepackets) + 1):
		left_packet = thepackets[i]['left'][:]
		right_packet = thepackets[i]['right'][:]
		correct_order = list_check(left_packet, right_packet, 2)
		if correct_order == 1:
			indices_sum += i
		elif correct_order == 2:
			print("there is a problem")
	return indices_sum



def list_check(left, right, order):
	''' takes two lists and checks for a next then pops and compares '''
	# order - 0 - out of order, 1 - in order, 2 - indeterminate
	print("starting list check - left: {}  right:{}".format(left, right))

	while order == 2:
		# rule 1 - if left runs out first then in right order
		if len(left) != 0:
			if len(right) == 0:
				#right ran out first
				print("right ran out first")
				order = 0
				return order
		else:
			# left ran out first
			print("left ran out first")
			order = 1
			return order
		# two not empty lists of so take first value
		# rule 3 if list take first value
		subleft = left.pop(0)
		subright = right.pop(0)
		order = check_popped_result(subleft, subright, 2)

	return order


def check_popped_result(left, right, order):
	''' recursive function to check result or go deeper - returns order '''
	# rule 2 - if both are integers left less than right is proper order
	print("... checking popped - left: {}  right:{}".format(left, right))
	if type(left) == type(right):
		# same types
		if type(left) == type(int()):
			# both are integers
			if left < right:
				order = 1
			elif left > right:
				order = 0
			else:
				# equal so indeterminate, check next in list
				order = 2

		elif type(left) == type(list()):
			# have two lists
			order = list_check(left, right, 2)

	else:
		# different types
		# rule 4 - if different types - find integer and convert it to list then retry
		if type(left) == type(int()):
			newleft = [left]
			newright = right
			print("different type, making list of left: {}".format(newleft))
		else:
			newright = [right]
			newleft = left
			print("different type, making list of right: {}".format(newright))
		# retry with new lists
		order = list_check(newleft, newright, 2)

	return order














