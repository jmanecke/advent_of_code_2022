''' rucksack rearrange day 3 '''

# put in the test data set to can run checks with it
test_list = [
	"vJrwpWtwJgWrhcsFMMfFFhFp",
	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
	"PmmdzqPrVvPwwTWBwg",
	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
	"ttgJtRGJQctTZtZT",
	"CrZsJsPPZsGzwwsLwLmpwMDw"
	]

# pull in the list and strip off /n's
def file_input(filename = 'input_day3.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerows = infile.read().splitlines()
	return filerows


def split_compartments(filerows):
	''' for each row break it in half to left and right compartment contents'''
	compartments = []
	for wholestring in filerows:
		left_compartment = wholestring[:int(len(wholestring)/2)]
		right_comprtment = wholestring[int(len(wholestring)/2):]
		compartments.append([left_compartment, right_comprtment])
	return compartments


def common_items(comp1, comp2):
	''' provide two strings (each compartments inventory) get back the item in common '''
	commonset = set(comp1)&set(comp2)
	if len(commonset) != 1:
		print("error, expecting only one commmon character")
		return
	# convert srings to sets then & together and get the single string in common
	common_char = list(commonset)[0]
	return common_char


def find_group_badge(group_rows):
	''' given a list of three elves rucksack contents (a group) find the common item between each sack, which is their badge '''
	commonset = set(group_rows[0])&set(group_rows[1])&set(group_rows[2])
	if len(commonset) != 1:
		print("error, expecting only one commmon character")
		return
	# convert srings to sets then & together and get the single string in common
	badge_char = list(commonset)[0]
	return badge_char


def get_priority(character):
	''' given a character a-z or A-Z return integer priority based on rules '''
	# validate 
	if not character.isalpha():
		print("invalid character input")
		return 99999
	if character.isupper():
		priority = ord(character) - 64 + 26
	else:
		priority = ord(character) - 96
	return priority

def calc_p1_priority(filerows):
	''' go through each row and sum priority '''
	compartments = split_compartments(filerows)
	priority_sum = 0
	for sack in compartments:
		common_char = common_items(sack[0], sack[1])
		priority_sum += get_priority(common_char)
	return priority_sum

def calc_p2_priority(filerows):
	''' go through three row elve groups and find common badge then priority and sum that'''
	priority_sum = 0
	for i in range(0,len(filerows),3):
		elvegroup = filerows[i:i+3]
		badge_char = find_group_badge(elvegroup)
		priority_sum += get_priority(badge_char)
	return priority_sum


def give_answer():
	''' just run this to spit out an answer '''
	therows = file_input()
	print("The priorty sum for part one is: {}".format(calc_p1_priority(therows)))
	print("The priorty sum for part two is: {}".format(calc_p2_priority(therows)))
	return