''' rucksack rearrange day 3 '''

# pull in the list and strip off /n's, the break in half, each row become a list of three strings
def file_input(filename = 'input_day3.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerawrows = infile.readlines()
	filerows = []
	for row in filerawrows:
		wholestring = row.strip()
		left_compartment = wholestring[:int(len(wholestring)/2)]
		right_comprtment = wholestring[int(len(wholestring)/2):]
		filerows.append([wholestring, left_compartment, right_comprtment])

	return filerows

