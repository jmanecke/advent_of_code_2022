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
	for i in range(0, len(notes_lines),7):
		if not re.search(r'\bMonkey\b', notes_lines[i]):
			return "Data is not as we expect"
		monkeyno = re.findall(r'\b\d+\b', notes_lines[i])[0]
		start_strings = re.findall(r'\b\d+\b', notes_lines[i+1])
		start_list = []
		for equipment in start_strings:
			worry_level = int(equipment)
			start_list.append(worry_level)
		theoperation = operation_parse(notes_lines[i+2])
		test_number = int(re.findall(r'\b\d+\b', notes_lines[i+3])[0])
		true_throw = re.findall(r'\b\d+\b', notes_lines[i+4])[0]
		false_throw = re.findall(r'\b\d+\b', notes_lines[i+5])[0]
		# create a dictionary for each monkey
		monkeying[monkeyno] = {
			"equipment": start_list,
			"opp_type": theoperation[0],
			"opp_magnitude": theoperation[1],
			"test_number": test_number,
			"true_throw": true_throw,
			"false_throw": false_throw,
			"number_inspected": 0
		}
	return monkeying


def operation_parse(operation):
	'''parses an operation string'''
	print("the operation string is:")
	print(operation)
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

def play_game(monkeying, rounds=20):
	''' runs through rounds number of the game '''
	for round in range(0,20):
		print("round {}".format(round))
	# buld list of active monkeys
	number_inspections = []
	for monkey in monkeying.keys():
		number_inspections.append(monkeying[monkey]['number_inspected'])

	return number_inspections


def round_move(monkeying):
	'''go through one game round'''
	for monkey in monkeying.keys():
		# skip a monkey's turn if they have not equipment
		if len(monkeying[monkey]['equipment']) != 0:
			monkey_divisor = monkeying[monkey]['test_number']
			to_true = monkeying[monkey]['true_throw']
			to_false = monkeying[monkey]['false_throw']
			opp_type = monkeying[monkey]['opp_type']
			opp_mag = monkeying[monkey]['opp_magnitude']

			# go trhough each item in turn
			for item in monkeying[monkey]['equipment']:
				monkeying[monkey]['equipment'].remove(item)
				monkeying[monkey]['number_inspected'] += 1
				inspection_worry = inspect_item(item, opp_type, opp_mag)
				test_worry = inspection_worry // 3
				if test_worry % monkey_divisor == 0:
					monkeying[to_true]['equipment'].append(test_worry)
				else:
					monkeying[to_false]['equipment'].append(test_worry)
		#end of one monkey's turn
	# end of the round
	return monkeying


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


def give_answer():
	'''just spit out the answers'''
	import monkeys
	filelines = monkeys.file_input(monkeys.testfile)
	monkeydict = monkeys.process_lines(filelines)
	play_game(monkeydict)





