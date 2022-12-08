''' classes to model a directory tree with files '''

# assumptions
#  only discovering files and directories - meaning only adding
#  no removing directories or files
#  only directory that can have no parent is root '/' - no lost+found

class Directory:
	'''directory object has a parent, size attribute and holds other direcotries and files'''

	def __init__(self, directory_name, parent_dir):
		'''initially empty with no size and only a parent'''
		self.total_size = 0
		self.directory_name = directory_name
		if directory_name == '/':
			self.parent_dir = 'EMPTY'
		else:
			self.parent_dir = parent_dir
			parent_dir.add_child(self)
		self.file_names = []
		self.file_sizes = []
		self.subdirectory_reference = []
		self.subdirectory_names = []
		return


	def calculate_size(self):
		''' calculates the size of the directory '''
		calc_size = 0
		# first add up files
		for filesize in self.file_sizes:
			calc_size += filesize
		# then add contained directories (assume they are accurate)
		for subdirectory in self.subdirectory_reference:
			calc_size += subdirectory.total_size
		self.total_size = calc_size
		return calc_size


	def add_size_to_parent(self, size_add):
		''' adds value to size of parent and walks up unless root '''
		if self.directory_name == '/':
			return
		else:
			self.parent_dir.total_size += size_add
			self.parent_dir.add_size_to_parent(size_add)


	def add_files(self, filearray):
		'''adds list of files to the directory'''
		# file array is a list of name/size tuples
		total_size_add = 0
		for filedata in filearray:
			self.file_names.append(filedata[0])
			self.file_sizes.append(filedata[1])
			total_size_add += filedata[1]
		#update size of this directory
		self.total_size += total_size_add

		# if not root, walk up to root and add size to directories
		if self.directory_name == '/':
			return
		else:
			self.add_size_to_parent(total_size_add)
		return


	def add_child(self, directory):
		'''adds a single directory reference into this directory'''
		# check if directory already in this directory if so noop
		if directory in self.subdirectory_reference:
			print("Directory already in this directory")
			return
		self.subdirectory_reference.append(directory)
		self.subdirectory_names.append(directory.directory_name)
		return


	def get_subdirectory_reference(self, sub_name):
		''' given a strint name of a subdirectory return the reference '''
		for i in range(0,len(self.subdirectory_reference)):
			if self.subdirectory_names[i] == sub_name:
				return self.subdirectory_reference[i]
		return "directory does not exist"


	def subdirectory_list(self, directory_list):
		''' start at sub and list name and size of each subdirectory recursively '''
		# start with current directory
		add_tuple = (self.directory_name, self.total_size)
		directory_list.append(add_tuple)
		# now go to each subdirectory
		for reference in self.subdirectory_reference:
			reference.subdirectory_list(directory_list)
		return directory_list