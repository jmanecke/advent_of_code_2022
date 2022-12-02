''' rock paper scissors day 2 '''

# writing the parameters here, could also just call from command line
filename = 'input_day2.data'

# send in an empty list and the filename
def file_input(filename = 'input_day2.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		filerows = infile.readlines()

	return filerows

def score_round(roundrow = 'emptystring'):
	''' input the row and return a score for that play '''
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

def myscore_total(filerows):
	''' given the rows figure total score if you played the rows '''
	total_score = 0
	for row in filerows:
		total_score += rps.score_round(row)

	return total_score