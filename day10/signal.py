''' I'm carrying a literal cathode ray tube device - old school!'''

# writing the parameters here, could also just call from command line
filename = 'input_day10.data'
testfile = 'test_day10.data'

# making a data strucure such that it's a list with one entry for each cycle
# 0 - the cycle before anything happens - written as a Noop, state is 1
# each entry is a command tuple and the state at the end of the cycle
# entry - [ (op_type, command_value), state ]
#	optype - 0 - noOp, 1 - first cycle of an addx, 2 - second cycle of an addx
#	command value - 0 or noop or first cycle of an addx, value for second cycle
#	state - the state info at end of the cycle
#
#

# pull in the processor output format it for use
def file_input(filename = 'input_day10.data'):
	''' Reads in files and appends rows to list of rows then does more '''
	with open(filename, 'r') as infile:
		processor_lines = infile.read().splitlines()
	return processor_lines


def input_parse(processor_lines):
	'''go line by line and make a cycle based list'''
	cycles = [[(0,0),1]]
	# two valid commands addx and noop
	for command in processor_lines:
		first_parse = command.split()
		if first_parse[0] == 'noop':
			cycles.append([(0,0),0])
		elif first_parse[0] == 'addx':
			if first_parse[1] == 0:
				print("found a zero value addx")
			cycles.append([(1,0),0])
			cycles.append([(2,int(first_parse[1])),0])
		else:
			print("Bad data found")

	return cycles


def calculate_register(cycles):
	''' go through the cycles and calculate the register value at the end of each cycle and update it '''
	for i in range(1,len(cycles)):
		cycles[i][1] = cycles[i-1][1] + cycles[i][0][1]
	return cycles

def sum_selected_strengths(cycles, start=20, end=225, interval=40):
	''' given a list of cycles, calculate strenght DURRING each and sum them '''
	strength_sum = 0
	for i in range(start, end, interval):
		strength_sum += cycles[i-1][1] * i
	return strength_sum


	

