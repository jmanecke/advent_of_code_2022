''' rucksack rearrange day 3 '''

test_list = [
	"vJrwpWtwJgWrhcsFMMfFFhFp",
	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
	"PmmdzqPrVvPwwTWBwg",
	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
	"ttgJtRGJQctTZtZT",
	"CrZsJsPPZsGzwwsLwLmpwMDw"
	]

# pull in the list and strip off /n's, then break in half, each row become a list of three strings
# also figure out what is in common
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
	''' provide two string (each compartments inventory) get back the item common '''
	commonset = set(comp1)&set(comp2)
	if len(commonset) != 1:
		print("error, expecting only one commmon character")
		return
	# convert srings to sets then & together and get the single string in common
	common_char = list(commonset)[0]
	return common_char


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

