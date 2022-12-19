''' what sides are not connected to another cube '''

# not connected means there is no cube in the position adjoining the side
# for each cube there are six position to check to see if another cube exists

# writing the parameters here, could also just call from command line
filename = 'input_day18.data'
testfile = 'test_day18.data'

def file_input(filename = 'input_day18.data'):
	''' read in the file lines and parse into a list of coordinate tuples '''
	with open(filename, 'r') as infile:
		coordinate_lines = infile.read().splitlines()
	coordinates = []
	for coordinate_string in coordinate_lines:
		coord_string_list = coordinate_string.split(',')
		xval = int(coord_string_list[0])
		yval = int(coord_string_list[1])
		zval = int(coord_string_list[2])
		coordinates.append((xval, yval, zval))
	return coordinates


def count_free_sides(coordinates, exterior_set):
	'''go through coordinates and count free sides'''
	free_sides = 0
	exterior_sides = 0
	for lavadrop in coordinates:
		check_result = check_one_cube(lavadrop, coordinates, exterior_set)
		sidesfree = check_result[0]
		free_sides += sidesfree
		exteriorfree = check_result[1]
		exterior_sides += exteriorfree
	return free_sides, exterior_sides


def check_one_cube(lavadrop, coordinates, exterior_set):
	'''for one lavadrop coordinate, count number of free sides'''
	free_sides = 0
	exterior_sides = 0
	test_xplus = (lavadrop[0] + 1, lavadrop[1], lavadrop[2])

	if test_xplus not in coordinates:
		free_sides += 1
		if test_xplus in exterior_set:
			exterior_sides += 1

	test_yplus = (lavadrop[0], lavadrop[1] + 1, lavadrop[2])
	if test_yplus not in coordinates:
		free_sides += 1
		if test_yplus in exterior_set:
			exterior_sides += 1

	test_zplus = (lavadrop[0], lavadrop[1], lavadrop[2] + 1)
	if test_zplus not in coordinates:
		free_sides += 1
		if test_zplus in exterior_set:
			exterior_sides += 1

	test_xminus = (lavadrop[0] - 1, lavadrop[1], lavadrop[2])
	if test_xminus not in coordinates:
		free_sides += 1
		if test_xminus in exterior_set:
			exterior_sides += 1

	test_yminus = (lavadrop[0], lavadrop[1] - 1, lavadrop[2])
	if test_yminus not in coordinates:
		free_sides += 1
		if test_yminus in exterior_set:
			exterior_sides += 1

	test_zminus = (lavadrop[0], lavadrop[1], lavadrop[2] - 1)
	if test_zminus not in coordinates:
		free_sides += 1
		if test_zminus in exterior_set:
			exterior_sides += 1

	return free_sides, exterior_sides


def find_boundaries(coordinates):
	''' find a cube that bounds the entire drop with at least one empty space '''
	x_coords = set()
	y_coords = set()
	z_coords = set()
	for lavadrop in coordinates:
		x_coords.add(lavadrop[0])
		y_coords.add(lavadrop[1])
		z_coords.add(lavadrop[2])
	x_lower = min(x_coords)
	x_upper = max(x_coords)
	y_lower = min(y_coords)
	y_upper = max(y_coords)
	z_lower = min(z_coords)
	z_upper = max(z_coords)
	boundary = (x_lower, x_upper, y_lower,y_upper, z_lower, z_upper)
	return boundary


def empty_map_data(boundary):
	''' create an empty data structure to use for mapping '''
	map_data = {}
	# for each coordinate in map data, have one of the folloiwng values:
	# 0 - unknown, 1 - lava, 2 - exterior space, 3 - trapped bubble

	for x in range(boundary[0]-1, boundary[1]+2):
		for y in range(boundary[2]-1, boundary[3]+2):
			for z in range(boundary[4]-1, boundary[5]+2):
				coordinate = (x,y,z)
				map_data[coordinate] = 0
	return map_data


def add_lava(map_data, coordinates):
	''' mark the spaces in map data that are lava '''
	# also make a set of lava coordinates (really just the input data)
	lava_set = set()
	for lavadrop in coordinates:
		map_data[lavadrop] = 1
		lava_set.add(lavadrop)
	return map_data, lava_set

def map_space(coordinates):
	''' map the empty space surrounding the drop '''
	boundary = find_boundaries(coordinates)
	blank_map = empty_map_data(boundary)
	lava_result = add_lava(blank_map, coordinates)
	lava_map = lava_result[0]
	lava_set = lava_result[1]

	# now start on outside and check touching space for lava or exterior
	map_start = (boundary[0]-1, boundary[2]-1, boundary[4]-1)
	exterior_set = set()
	exterior_set.add(map_start)
	# queue spaces to check
	# if a space is not lava and touches an exterior space, it is also an exterior space
	map_queue = [map_start]
	while map_queue:
		current_space = map_queue.pop(0)
		#evaluate space and add adjacents to queue
		evaluate_adjacents(current_space, lava_map, boundary, exterior_set, map_queue)

	# mark any remaining as interior
	interior_set = set()
	for coordinate in lava_map.keys():
		if lava_map[coordinate] == 0:
			# not visited and not lava so interior
			lava_map[coordinate] = 3
			interior_set.add(coordinate)

	return lava_map, lava_set, exterior_set, interior_set


def evaluate_adjacents(current_space, map_data, boundary, exterior_set, map_queue):
	''' for a single space check adjacents if not lava mark extrior and enque '''
	#don't check if on the map boundary - one beyond boundary numbers
	if current_space[0] != boundary[0]-1:
		left = (current_space[0] -1, current_space[1], current_space[2])
		if map_data[left] == 0:
			map_data[left] = 2
			map_queue.append(left)
			exterior_set.add(left)

	if current_space[0] != boundary[1]+1:
		right = (current_space[0] +1, current_space[1], current_space[2])
		if map_data[right] == 0:
			map_data[right] = 2
			map_queue.append(right)
			exterior_set.add(right)

	if current_space[1] != boundary[2]-1:
		below = (current_space[0], current_space[1] - 1, current_space[2])
		if map_data[below] == 0:
			map_data[below] = 2
			map_queue.append(below)
			exterior_set.add(below)

	if current_space[1] != boundary[3]+1:
		above = (current_space[0], current_space[1] + 1, current_space[2])
		if map_data[above] == 0:
			map_data[above] = 2
			map_queue.append(above)
			exterior_set.add(above)

	if current_space[2] != boundary[4]-1:
		backward = (current_space[0], current_space[1], current_space[2] - 1)
		if map_data[backward] == 0:
			map_data[backward] = 2
			map_queue.append(backward)
			exterior_set.add(backward)

	if current_space[2] != boundary[5]+1:
		forward = (current_space[0], current_space[1], current_space[2] + 1)
		if map_data[forward] == 0:
			map_data[forward] = 2
			map_queue.append(forward)
			exterior_set.add(forward)

	return


def give_answer():
	coordinates = file_input()
	themap_results = map_space(coordinates)
	lava_set = themap_results[1]
	exterior_set = themap_results[2]
	free_result = count_free_sides(lava_set, exterior_set)
	print("For part 1 there are {} free sides".format(free_result[0]))
	print("For part 2 there are {} free sides".format(free_result[1]))