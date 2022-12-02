''' rock paper scissors day 2 '''

# writing the parameters here, could also just call from command line
filename = 'input_day2.data'

# for part 2 use a dict of outcomes
# use the desired result as the first key which gets the outcome_score, then use the column1 to value
# to determine the play_score for playing the move what will achieve the outcome

outcome_matrix_p2 = {
	"X": {"outcome": "lose", "outcome_score": 0,
			"play_score": {
				"A": 3,
				"B": 1,
				"C": 2
				}
			},
	"Y": {"outcome": "draw", "outcome_score": 3,
			"play_score": {
				"A": 1,
				"B": 2,
				"C": 3
				}
			},
	"Z": {"outcome": "win", "outcome_score": 6,
			"play_score": {
				"A": 2,
				"B": 3,
				"C": 1
				}
			}
	}

# send in an empty list and the filename
def file_input(filename = 'input_day2.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerows = infile.readlines()

	return filerows

def score_round_one(roundrow = 'emptystring'):
	''' input the row and return a score for that play based on part 1 assumptions'''
	outcome_score = 0
	#play_score - score for what I played
	#outcome_score - score based on win lose or draw

	#start with what I played
	if roundrow[2] == 'X':
		# I played rock
		play_score = 1
		# check the win/lose/draw part
		if roundrow[0] == 'C':
			outcome_score = 6 # I win
		elif roundrow[0] == 'A': # a draw
			outcome_score = 3

	elif roundrow[2] == 'Y':
		# I played paper
		play_score = 2
		# check the win/lose/draw part
		if roundrow[0] == 'A':
			outcome_score = 6 # I win
		elif roundrow[0] == 'B': # a draw
			outcome_score = 3

	elif roundrow[2] == 'Z':
		# I played scissors
		play_score = 3
		# check the win/lose/draw part
		if roundrow[0] == 'B':
			outcome_score = 6 # I win
		elif roundrow[0] == 'C': # a draw
			outcome_score = 3

	else:
		print("data error in input - you didn't play anything")
		return

	round_score = play_score + outcome_score
	return round_score

def myscore_total_one(filerows):
	''' given the rows figure total score if you played the rows '''
	total_score = 0
	for row in filerows:
		total_score += score_round_one(row)

	return total_score


# adding a second set of functions for round two, could probably refactor the myscore_total_xxx function to use one for both

def score_round_two(roundrow = 'emptystring'):
	''' input the row and return a score for that play based on part 2 assumptions'''
	outcome_score = 0
	#play_score - score for what I played
	#outcome_score - score based on win lose or draw

	# much simpler here using the outcome dict

	col1 = roundrow[0]
	col2 = roundrow[2]
	outcome_score = outcome_matrix_p2[col2]['outcome_score']
	play_score = outcome_matrix_p2[col2]['play_score'][col1]
	round_score = play_score + outcome_score
	return round_score

def myscore_total_two(filerows):
	''' given the rows figure total score if you played the rows '''
	total_score = 0
	for row in filerows:
		total_score += score_round_two(row)

	return total_score

def give_answer():
	''' just run this to spit out an answer '''
	therows = file_input()
	print("The score for part one is: {}".format(myscore_total_one(therows)))
	print("The score for part two is: {}".format(myscore_total_two(therows)))

	return