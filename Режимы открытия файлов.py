from pprint import pprint

file_name = 'coding.txt'
file = open(file_name, mode='r')
file_conted = file.read()
file.close()
pprint(file_conted)
