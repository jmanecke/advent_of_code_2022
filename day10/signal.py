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

screen_test = []
line = "########################################"
for i in range(0,6):
	screen_test.append(line)

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


def give_answer():
	''' just run this to spit out an answer '''
	processor_lines = file_input()
	cycles = input_parse(processor_lines)
	calculate_register(cycles)
	print("The part 1 answer is: {}".format(sum_selected_strengths(cycles)))
	print()
	lines = calculate_screen(cycles)
	myscreen = build_screen(lines)
	print("The screen for part 2 is:")
	print()
	show_screen(myscreen)
	print()
	return


def show_screen(screen = screen_test):
	'''prints out a six line screen'''
	for i in range (0,6):
		print(screen[i])
	return


def calculate_screen(cycles):
	'''chooses whether pixels are on or off based on sprite position'''
	lines = []
	for l in range(0,6):
		screenlit = []
		for i in range(0,40):
			p2cycle = l * 40 + i
			sprite_pos = cycles[p2cycle][1]
			if i >= sprite_pos-1 and i <= sprite_pos+1: 
				screenlit.append(True)
			else:
				screenlit.append(False)
		lines.append(screenlit)
	return lines


def build_screen(lines):
	''' create strings out of the on off and build a screen '''
	'give lines of on/off make a screen of strings'
	ison = '#'
	isoff = ' '
	screen = []
	for line in lines:
		thestring = str()
		for character in line:
			if character:
				thestring += ison
			else:
				thestring += isoff
		screen.append(thestring)
	return screen