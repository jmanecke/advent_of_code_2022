''' clean up overlaps day 4 '''

# writing the parameters here, could also just call from command line
filename = 'input_day5.data'
testfile = 'test_day5.data'

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
	stack = {"total_stacks": total_stacks}
	# assuming stacks are numerically numbered and in ascending order, checks based on our data
	# create a reverse list of only the crates (leave off the numbers row)
	crate_strings = stackstrings[:-1]
	crate_strings.reverse()
	# start at bottom row and go up
	for craterow in crate_strings:
		# do cool things



	return stacks

def parse_craterow(craterow, rowlength):
	''' given a row of the crate input, parse it into a list, with OPEN for no crate '''
	row_crates = []
	# break it into groups of 4
	for i in range(0,rowlength, 4):
		crateletter = craterow[i:i+3].strip('[]')
		row_crates.append(crateletter)




def get_moves(movesstrings):
   ''' take the move list and parse it into list of move tuples '''

   return moveslist


def sort_crates(stacks, moveslist):
	''' goes through moves, makes them, returns resulting moved list '''


	return moved_list