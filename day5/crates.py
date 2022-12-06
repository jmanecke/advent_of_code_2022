''' clean up overlaps day 4 '''

import re

# writing the parameters here, could also just call from command line
filename = 'input_day5.data'
testfile = 'test_day5.data'

# the crates will be arranged into a dict of lists
# key - the stack number (as a string)
# for each key - list of strings, crate letter only - stripping off extraneuos brackets to avoid confusion
# the bottom crate is at the [-1] position, the top crate is at the [0] position
# example of what the stacks dict looks like for the test data
# stacks = {
#  "stack_names": ['1', '2', '3']
# 	"1": ['Z', 'N'],
#	"2": ['M', 'C', 'D'],
#	"3": ['P']
# }

# moves are a list of tuples, each move tuple has (int, str, str)
# int - # of crates to move, str - from stack, str - to stack

# note - works fine if stacks are numbers or letters


# pull in the list and strip off /n's
def file_input(filename = 'input_day5.data'):
	''' Reads in files and appends rows to list of rows slits into two based on empty line '''
	with open(filename, 'r') as infile:
		filerows = infile.read().splitlines()
	# find index of empty and make two lists of strings
	empty_row_index = filerows.index('')
	stackstrings = filerows[:empty_row_index]
	movesstrings = filerows[empty_row_index+1:]

	# do a quick check to make sure parsing makes sense in the file
	if len(filerows) != len(stackstrings) + len(movesstrings) +1:
		print("bad data beware!")
	else:
		print("Imported {} rows, {} describe the stacks, {} are moves".format(len(filerows), len(stackstrings), len(movesstrings)))

	return stackstrings, movesstrings


def get_crate_initial(stackstrings):
	''' take the crate info from the top and arrange it as a dict of stack lists '''
	# all rows are the same number of characters, last row defines the stack numbers
	rowlength = len(stackstrings[-1])
	stack_numbers = re.findall(r'\b\d+\b', stackstrings[-1])
	total_stacks = len(stack_numbers)
	# define stacks dict and put the total as a key
	stacks = {"stack_names": stack_numbers}
	# add empty lists for each key
	for stack_no in stack_numbers:
		stacks[stack_no] = []
	# assuming stacks are numerically numbered and in ascending order, checks based on our data
	# create a reverse list of only the crates (leave off the numbers row)
	crate_strings = stackstrings[:-1]
	crate_strings.reverse()
	# start at bottom row and go up
	for craterow in crate_strings:
		# get row as a list
		cratelist = parse_craterow(craterow, rowlength)
		# iterate through each stack
		for stack_no in stack_numbers:
			# append to list, skipping null ones
			addcrate = cratelist.pop(0)
			if len(addcrate.strip()) != 0:
				stacks[stack_no].append(addcrate)

	return stacks

def parse_craterow(craterow, rowlength):
	''' given a row of the crate input, parse it into a list, with OPEN for no crate '''
	row_crates = []
	# break it into groups of 4
	for i in range(0,rowlength, 4):
		crateletter = craterow[i:i+3].strip('[]')
		row_crates.append(crateletter)
	return row_crates


def get_moves(movesstrings):
   ''' take the move list and parse it into list of move tuples '''
   moves_list = []
   # go through each move and parse then add to list
   for onemove_string in movesstrings:
   	onemove_list = re.findall(r'\d+', onemove_string)
   	onemove_tuple = (
   		int(onemove_list[0]),
   		onemove_list[1],
   		onemove_list[2]
   		)
   	moves_list.append(onemove_tuple)
   return moves_list


def sort_crates(stacks, moveslist, model_no):
	''' goes through moves, makes them, returns resulting moved_stacks '''
	# model_no is the crane model number - 9000 or 9001
	if model_no == 9000:
		# move one crate at a time so pop and append
		for onemove in moveslist:
			for i in range(0,onemove[0]):
				stacks[onemove[2]].append(
					stacks[onemove[1]].pop()
					)
	elif model_no == 9001:
		# moving multiple crates at a time so slicing lists
		for onemove in moveslist:
			addpart = stacks[onemove[1]][-1*onemove[0]:]
			stacks[onemove[2]] += addpart
			del stacks[onemove[1]][-1*onemove[0]:]
	else:
		print("bad crane model")
	return stacks


def top_crates(stacks):
	''' given the stack dict, return a string of crates at top of each stack '''
	topletters = str()
	for stack_no in stacks["stack_names"]:
		topletters += stacks[stack_no][-1]
	return topletters


def give_answer():
	''' just run this to spit out an answer '''
	thestringrows = file_input()
	stacks = get_crate_initial(thestringrows[0])
	moves_list = get_moves(thestringrows[1])
	moved_stacks_p1 = sort_crates(stacks, moves_list, 9000)
	part1_topcrates = top_crates(moved_stacks_p1)
	# build new stack dict for p2
	p2_stacks = get_crate_initial(thestringrows[0])
	moved_stacks_p2 = sort_crates(p2_stacks, moves_list, 9001)
	part2_topcrates = top_crates(moved_stacks_p2)
	print("The top crates for part one are: {}".format(part1_topcrates))
	print("The top crates for part two are: {}".format(part2_topcrates))
	return