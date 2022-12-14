''' takes a list of elves with calories and finds the ones with the highest '''

# writing the parameters here, could also just call from command line
filename = 'input_day1.data'

# send in an empty list and the filename
def file_input(filename):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerows = infile.readlines()

	# add one empty to the end since the last row has a value
	filerows.append('\n')

	return filerows

def rows_to_elves(filerows):
	''' go through rows and sort into elves '''
	# count number of empty rows - only line \n, which is number of elves
	elf_number = 0
	for row in filerows:
		if row == '\n':
			elf_number += 1
	print("Number of elves is {}".format(elf_number))
	# really just a logic check for now, return list should have this many entries
	# go with a list where index number is elf number -1, value is an int sum of cals
	# cast as int to check and make sure we have all integers in the data set, should throw errors if not
	elf_total_cal = []
	caltotal = 0
	for row in filerows:
		if row != '\n':
			caltotal += int(row.strip())
		else:
			elf_total_cal.append(caltotal)
			caltotal = 0

	return elf_total_cal


def tell_me_about_it(elf_total_cal):
	''' given list of elves and calories tell max and sum of top three '''
	# make a copy so we preserve elf_total_cal if we want to do more with it
	worker_list = elf_total_cal[:]
	# sort the list
	worker_list.sort()

	print("The top calorie elf has {} calories".format(worker_list[-1]))

	topthree_cals = worker_list[-1] + worker_list[-2] + worker_list[-3]

	print("The top three elves have a total of {} calories".format(topthree_cals))

def give_answer():
	''' just run this to spit out an answer '''
	filerows = file_input(filename)
	elf_list = rows_to_elves(filerows)
	tell_me_about_it(elf_list)