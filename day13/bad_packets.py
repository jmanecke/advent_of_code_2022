'''packets are out of order so need to parse the input and figure out which ones are no good'''

import json

# writing the parameters here, could also just call from command line
filename = 'input_day13.data'
testfile = 'test_day13.data'


# pull in the raw packet ros and put them into an array of packet lines
def file_input(filename = 'input_day13.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		packetlines = infile.read().splitlines()
	thepackets = {}
	for i in range (2,len(packetlines)+3,3):
		packetcontents = {"left": json.loads(packetlines[i-2]), "right": json.loads(packetlines[i-1])}
		thepackets[int((i+1)/3)]=packetcontents
	return thepackets


def eval_packet_pairs(packet_dict):
	''' go through the pairs of packet and check if they are in the right order '''
	indices_sum = 0
	for i in range(1,len(packet_dict) + 1):
		# print()
		# print("starting on index {}".format(i))
		# print(packet_dict[i])
		left_packet = packet_dict[i]['left']
		right_packet = packet_dict[i]['right']
		# print("    left: {}".format(left_packet))
		# print("    right: {}".format(right_packet))
		correct_order = list_check(left_packet, right_packet)
		if correct_order == 1:
			indices_sum += i
			#print("in correct order, sum is: {}".format(indices_sum))
		elif correct_order == 2:
			print("there is a problem")
		#else:
			#print("not in correct order")
	return indices_sum


def eval_single_packet(packet_dict, packet_index):
	'''given a single packet index return the result'''
	left_packet = packet_dict[packet_index]['left']
	right_packet = packet_dict[packet_index]['right']
	correct_order = list_check(left_packet, right_packet)
	if correct_order == 1:
		print("in correct order")
	elif correct_order == 2:
		print("there is a problem")
	else:
		print("not in crrect order")
	return correct_order


def list_check(left, right):
	''' takes two lists and checks for a next then pops and compares '''
	# order - 0 - out of order, 1 - in order, 2 - indeterminate
	#print("starting list check - left: {}  right:{}".format(left, right))
	if type(left) != type(right) or type(left) != type(list()):
		print("Something went wrong")
	order = 2
	while order == 2:
		if len(left) == 0 and len(right) == 0:
			# both ran out at same time so indeterminate
			order = 2
			return order
		# rule 1 - if left runs out first then in right order
		elif len(left) != 0:
			if len(right) == 0:
				#right ran out first
				#print("right ran out first")
				order = 0
				return order
		else:
			# left ran out first
			#print("left ran out first")
			order = 1
			return order
		# two not empty lists of so take first value
		# rule 3 if list take first value
		subleft = left.pop(0)
		subright = right.pop(0)
		#print("start list check left: {} right: {}".format(subleft, subright))
		order = check_popped_result(subleft, subright)
		#print("ended list check left: {} right: {} and order {}".format(subleft, subright, order))

	return order


def check_popped_result(left, right):
	''' recursive function to check result or go deeper - returns order '''
	# rule 2 - if both are integers left less than right is proper order
	#print("... checking popped - left: {}  right:{}".format(left, right))
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
			order = list_check(left, right)

	else:
		# different types
		# rule 4 - if different types - find integer and convert it to list then retry
		if type(left) == type(int()):
			newleft = [left][:]
			newright = right[:]
			#print("different type, making list of left: {}".format(newleft))
		elif type(right) == type(int()):
			newright = [right][:]
			newleft = left[:]
			#print("different type, making list of right: {}".format(newright))
		else:
			print("something went wrong")
		# retry with new lists
		order = list_check(newleft, newright)

	return order


def give_answer():
	''' just run and print the answers '''
	thepackets = file_input()
	answer_p1 = eval_packet_pairs(thepackets)
	print("the part 1 answer is: {}".format(answer_p1))












