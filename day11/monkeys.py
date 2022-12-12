'''monkeys are throwing my stuff around'''

import re

# writing the parameters here, could also just call from command line
filename = 'input_day11.data'
testfile = 'test_day11.data'

# read in my notes and break them up by monkey
# because I take notes in yaml but not quite
def file_input(filename = 'input_day11.data'):
	''' Reads in files and appends rows to list of rows then does more '''
	with open(filename, 'r') as infile:
		notes_lines = infile.read().splitlines()
	return notes_lines

# assumptions on the input
# every 7th line is a monkey, each monkey has all values
#
def process_lines(notes_lines):
	monkeying = {}
	divisor_product = 1
	equipment_number = 0
	for i in range(0, len(notes_lines),7):
		if not re.search(r'\bMonkey\b', notes_lines[i]):
			return "Data is not as we expect"
		monkeyno = re.findall(r'\b\d+\b', notes_lines[i])[0]
		start_strings = re.findall(r'\b\d+\b', notes_lines[i+1])
		# assign an index only so we don't move the worry numbers, only the reference
		start_list = []
		pointer_list = []
		for equipment in start_strings:
			worry_level = int(equipment)
			start_list.append(worry_level)
			pointer_list.append(equipment_number)
			equipment_number += 1
		theoperation = operation_parse(notes_lines[i+2])
		test_number = int(re.findall(r'\b\d+\b', notes_lines[i+3])[0])
		divisor_product = divisor_product * test_number
		true_throw = re.findall(r'\b\d+\b', notes_lines[i+4])[0]
		false_throw = re.findall(r'\b\d+\b', notes_lines[i+5])[0]
		# create a dictionary for each monkey
		monkeying[monkeyno] = {
			"initial_equipment": start_list,
			"equipment_pointers": pointer_list,
			"opp_type": theoperation[0],
			"opp_magnitude": theoperation[1],
			"test_number": test_number,
			"true_throw": true_throw,
			"false_throw": false_throw,
			"number_inspected": 0
		}
	return monkeying, divisor_product

def build_worry_dict(monkeying):
	'''build a dict of integers for each equipment pointer'''
	worry_counts = {}
	worry_index = 0
	#iterate through monkeys and build the dict
	for monkey in monkeying.keys():
		for worry_score in monkeying[monkey]['initial_equipment']:
			worry_counts[worry_index] = worry_score
			worry_index += 1
	return worry_counts


def operation_parse(operation):
	'''parses an operation string'''
	if operation.strip() == 'Operation: new = old * old':
		opp_type = 'power'
		mag = 2
	elif operation[23] == '+':
		opp_type = 'add'
		mag = int(re.findall(r'\b\d+\b', operation)[0])
	elif operation[23] == '*':
		opp_type = 'multiply'
		mag = int(re.findall(r'\b\d+\b', operation)[0])
	else:
		print("Data problem on operation parsing")

	theoperation = [opp_type, mag]
	return theoperation

def play_game(monkeying, worry_counts, divisor_product, part, rounds=20):
	''' runs through rounds number of the game '''
	for round in range(0,rounds):
		if part == 'p1' or (part == 'p2' and round %100 == 0):
			print("round {}".format(round))
		round_result = round_move(monkeying, worry_counts, divisor_product, part)
		monkeying = round_result[0]
		worry_counts = round_result[1]
	# buld list of active monkeys
	number_inspections = []
	for monkey in monkeying.keys():
		number_inspections.append(monkeying[monkey]['number_inspected'])
	number_inspections.sort()
	monkey_business = number_inspections[-1] * number_inspections[-2]
	return monkey_business


def round_move(monkeying, worry_counts, divisor_product, part):
	'''go through one game round'''
	if part == 'p2':
		worry_divisor =1
	else:
		worry_divisor = 3
	for monkey in monkeying.keys():
		#print("Monkey {} moves now".format(monkey))
		# skip a monkey's turn if they have no equipment
		if len(monkeying[monkey]['equipment_pointers']) != 0:
			monkey_divisor = monkeying[monkey]['test_number']
			to_true = monkeying[monkey]['true_throw']
			to_false = monkeying[monkey]['false_throw']
			opp_type = monkeying[monkey]['opp_type']
			opp_mag = monkeying[monkey]['opp_magnitude']

			# go through each item in turn
			#print("the monkeys equipment is {}".format(monkeying[monkey]['equipment']))
			while len(monkeying[monkey]['equipment_pointers']) != 0:
				monkeying[monkey]['number_inspected'] += 1
				item_pointer = monkeying[monkey]['equipment_pointers'].pop(0)
				item = worry_counts[item_pointer]
				inspection_worry = inspect_item(item, opp_type, opp_mag)
				pre_test_worry = inspection_worry // worry_divisor
				test_worry = pre_test_worry % divisor_product
				worry_counts[item_pointer] = test_worry
				if test_worry % monkey_divisor == 0:
					monkeying[to_true]['equipment_pointers'].append(item_pointer)
				else:
					monkeying[to_false]['equipment_pointers'].append(item_pointer)
			# end of one item
		#end of one monkey's turn
		#print("end of turn for monkey {}".format(monkey))
		#print()
	# end of the round
	return monkeying, worry_counts


def inspect_item(item, opp_type, opp_mag):
	''' perform the opp and return an integer '''
	if opp_type == 'power':
		opp_result = item ** opp_mag
	elif opp_type == 'add':
		opp_result = item + opp_mag
	elif opp_type == 'multiply':
		opp_result = item * opp_mag
	else:
		print("bad operation requested")
	return opp_result


def show_monkeys(monkeydict):
	'''print out the current monkeys and their sate'''
	for monkey in monkeydict.keys():
		print("Monkey number " + monkey)
		print("init_equip:  {}".format(monkeydict[monkey]['initial_equipment']))
		print("equip_point: {}".format(monkeydict[monkey]['equipment_pointers']))		
		print("opp_type:    {}".format(monkeydict[monkey]['opp_type']))
		print("opp_magn:    {}".format(monkeydict[monkey]['opp_magnitude']))
		print("test_number: {}".format(monkeydict[monkey]['test_number']))
		print("true_throw:  {}".format(monkeydict[monkey]['true_throw']))
		print("false_throw: {}".format(monkeydict[monkey]['false_throw']))
		print("number_insp: {}".format(monkeydict[monkey]['number_inspected']))
		print()
		print()
	return

def give_answer(part = 'p1', filename = 'input_day11.data'):
	'''just spit out the answers'''
	import monkeys
	filelines = file_input(filename)
	process_result = process_lines(filelines)
	monkeydict = process_result[0]
	divisor_product = process_result[1]
	worry_counts = build_worry_dict(monkeydict)
	if part == 'p1':
		rounds = 20
	elif part == 'p2':
		rounds = 10000
	else:
		return "you used and invalid game part"
	monkey_business = play_game(monkeydict, worry_counts, divisor_product, part, rounds)
	print("The level of monkey business, based on {} rules, is {}".format(part, monkey_business))

	return



