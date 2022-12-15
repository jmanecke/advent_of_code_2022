''' crazy elf device is out of space so analyze the file systems storage use '''

import filetree

# assumptions
# only two commands are cd and ls - have a check function to validate
# ls command takes not parameters, meaning it's just "ls" and lists contents of the current directory
# ls ouput takes two forms
#   file - starts with an integer size then has a filename
#   directory - starts with dir then has a directory name
# cd always succeeds - no responses like "directory does not exist" or similar


# writing the parameters here, could also just call from command line
filename = 'input_day7.data'
testfile = 'test_day7.data'

# pull in the terminal list and strip off /n's
def file_input(filename = 'input_day7.data'):
	''' Reads in files and appends rows to list of rows '''
	with open(filename, 'r') as infile:
		termainal_output = infile.read().splitlines()
	return termainal_output


def only_two_commands(termainal_output):
	''' assumes input data only has two commands - check data for that '''
	for outputline in termainal_output:
		if outputline[:1] == '$' and (outputline[:4] != '$ ls' and outputline[:4] != '$ cd'):
			print("bad commands in data set")
			return False
	print("Only two commands found are $ ls and $ cd")
	return True


def build_tree(terminal_output):
	''' reads through terminal output and populates the filetree objects '''
	# check if bad and stop
	if not only_two_commands(terminal_output):
		return "there is a data problem"

	# instantiate the root to start and remove it from the output
	rootdir = filetree.Directory('/', 'EMPTY')
	currentdir = rootdir
	del terminal_output[0]

	for outputline in terminal_output:
		if outputline[:4] == '$ cd':
			# we have a cd command
			cd_destination = outputline[4:].strip()
			if cd_destination == '..':
				# going up
				if currentdir.directory_name == '/':
					print("ERROR - can't go above root, ignoring")
				else:
					nextdir = currentdir.parent_dir
			else:
				#going down, retrieve subdirectory reference from current directory
				nextdir = currentdir.get_subdirectory_reference(outputline[4:].strip())
			currentdir = nextdir
		elif outputline[:4] != '$ ls':
			# we have an ls command output
			parsed_output = outputline.split()
			if parsed_output[0] == 'dir':
				# check if already exists as subdirectory
				if parsed_output[1] in currentdir.subdirectory_names:
					print("going into directory already created")
				else:
					#create a new directory under current
					newdir = filetree.Directory(parsed_output[1], currentdir)
			else:
				# add a file to current directory
				newfile_array = [(parsed_output[1], int(parsed_output[0]))]
				currentdir.add_files(newfile_array)
	return rootdir


def dir_size_check(rootdir, topsize = 100000):
	'''search a directory tree for directories equal or less than a certain size'''
	starter_list = []
	directory_attr_list = rootdir.subdirectory_list(starter_list)
	#iterate through directories
	size_sum = 0
	for directory in directory_attr_list:
		if directory[1] <= 100000:
			size_sum += directory[1]
	return size_sum


def smallest_to_delete(rootdir, needed_space = 30000000, total_space = 70000000):
	'''find smalles directory that if deleted, would provide needed space'''
	required_size = rootdir.total_size - (total_space - needed_space)
	print("required space is {}".format(required_size))

	starter_list = []
	directory_attr_list = rootdir.subdirectory_list(starter_list)
	#make a list of just the sizes
	dir_size_list = []
	for directory in directory_attr_list:
		dir_size_list.append(directory[1])
	dir_size_list.sort()
	for dir_size in dir_size_list:
		if dir_size >= required_size:
			return dir_size
	return "no directories work"


def give_answer():
	''' just run this to spit out an answer '''
	terminal_output = file_input()
	rootdir = build_tree(terminal_output)
	howbig = dir_size_check(rootdir)
	print("The sum of sizes for part 1 is {}".format(howbig))
	smallest = smallest_to_delete(rootdir)
	print("The directory size for part 2 is: {}".format(smallest))
	return