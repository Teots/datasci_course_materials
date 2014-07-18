import MapReduce
import sys

"""
Social Network
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: person
	# value: friend
	key = record[0]
	value = record[1]
	mr.emit_intermediate(key, value)
	mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence document_ids
	mapping = {}
	for v in list_of_values:
		if v not in mapping:
			mapping[v] = 1
		else:
			mapping[v] += 1

	for v in list_of_values:
		if mapping[v] != 2:
			mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
