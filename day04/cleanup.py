''' clean up overlaps day 4 '''

# writing the parameters here, could also just call from command line
filename = 'input_day4.data'
testfile = 'test_day4.data'

# pull in the list and strip off /n's
def file_input(filename = 'input_day4.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerows = infile.read().splitlines()
	return filerows


def input_process(filerows):
	''' parses the rows into the two elves and does some data checks '''

	parsed_rows = []
	# just spliting it directly to find commas and dashes assuming data is sane, could use csv or similar but this is very simple
	# break each row into a list [a, b, c, d]
	#  a - start of range first elf
	#  b - end of range first elf
	#  c - start of range second elf
	#  d - end of range second elf
	for row in filerows:
		twoelves = row.split(',',2)
		result_elf1 = twoelves[0].split('-',2)
		result_elf2 = twoelves[1].split('-',2)
		string_row = (result_elf1 + result_elf2)
		# convert strings to int, will fail if data is bad
		int_row = []
		for row in string_row:
			int_row.append(int(row))
		parsed_rows.append(int_row)

	return parsed_rows


def find_the_overlaps(parsed_rows, check_type):
	''' count number of overlapping elf pairs whether full or part'''
	overlap_count = 0
	if check_type == 'full':
		for elfpair in parsed_rows:
			if check_full_overlap(elfpair):
				overlap_count += 1
	elif check_type == 'part':
		for elfpair in parsed_rows:
			if check_part_overlap(elfpair):
				overlap_count += 1
	else:
		return "Bad overlap Type"
	
	return overlap_count


def check_full_overlap(elfpair):
	''' given an elfpair list return true if either fully overlaps '''
	isoverlap = False
	# check first range fully in second range
	if elfpair[0] >= elfpair[2] and elfpair[1] <= elfpair[3]:
		isoverlap = True
	# check second range fully in first
	if elfpair[2] >= elfpair[0] and elfpair[3] <= elfpair[1]:
		isoverlap = True
	# result of function is True if full overlap
	return isoverlap


def check_part_overlap(elfpair):
	''' given an elfpair list return true if there is a partial overlap '''
	isoverlap = True
	# check first range is below second
	if elfpair[1] < elfpair[2]:
		isoverlap = False
	# check second range below first
	if elfpair[3] < elfpair[0]:
		isoverlap = False
	# result of function is True if any overlap
	return isoverlap


def give_answer():
	''' just run this to spit out an answer '''
	therows = file_input()
	parsed_lists = input_process(therows)
	print("The number of overlaps for part one is: {}".format(find_the_overlaps(parsed_lists,'full')))
	print("The number of overlaps for part two is: {}".format(find_the_overlaps(parsed_lists,'part')))
	return