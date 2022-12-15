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
			packetcontents = {"line1": packetlines[i-2], "line2": packetlines[i-1]}
			thepackets[int((i+1)/3)]=packetcontents
	return thepackets


def eval_packet_pairs(thepackets):
	''' go through the pairs of packet and check if they are in the right order '''
	indices_sum = 0
	for i in range(1,len(thepackets +1)):
		right_order = eval_packet(packet_pair)
		if right_order == True:
			indices_sum += i
	return indices_sum


def eval_pairs(packet_pair):
	''' given a single packet pair go through all the checks for in in order '''
	right_order = False
	# check #1 - if both are integers
	left = packet_pair['line1'][0]
	right = packet_pair['line2'][0]
	if type(left) == type(right):
		if type(left) == type(int()):
			if left < right:
				right_order = True
				return





