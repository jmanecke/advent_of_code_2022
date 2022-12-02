''' takes a csv list of elves with calories and finds the ones with the highest '''

import csv

# writing the parameters here, could also just call from command line
filerows = []
filename = 'input_day1.data'

# pulled some code I had to parse csv files and hacked it up. Quick solution. Change to do without the csv
def file_input(filerows, filename):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		reader = csv.reader(infile)
		# 

		for row in reader:
				filerows.append(row)
		# add one empty to the end since the last row has a value
		filerows.append([])

	return

def rows_to_elves(filerows):
	''' go through rows and sort into elves '''
	# count number of empty rows, which is number of elves
	elf_number = 0
	for row in filerows:
		if len(row) == 0:
			elf_number += 1
	print("Number of elves is {}".format(elf_number))
	# really just a logic check for now, return list should have this many entries
	# go with a list where index number is elf number -1, value is an int sum of cals
	elf_total_cal = []
	caltotal = 0
	for row in filerows:
		if len(row) != 0:
			caltotal += int(row[0])
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
	file_input(filerows, filename)
	elf_list = rows_to_elves(filerows)
	tell_me_about_it(elf_list)