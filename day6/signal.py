''' signal tuning by finding data stream pakcets '''

# writing the parameters here, could also just call from command line
filename = 'input_day6.data'
testfile = 'test_day6.data'

teststream1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
teststream2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
teststream3 = 'nppdvjthqldpwncqszvftbrmjlhg'
teststream4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
teststream5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def file_input(filename = 'input_day65ata'):
    ''' Reads in files and strips any /n '''
    with open(filename, 'r') as infile:
        filestream = infile.read().splitlines()
        filestream.strip()
    return filestream

def find_unique_marker(inputstream, marker_length):
    ''' take input stream and look for a marker length characters wihtout repeat '''
    for i in range(0,len(inputstream)):
        if len(set(inputstream[i:i+marker_length])) == marker_length:
            print("Marker at postition {}".format(i+marker_length))
            return i + marker_length
