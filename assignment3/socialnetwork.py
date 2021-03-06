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
	mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence document_ids
	total = 0
	for v in list_of_values:
		total += 1
	mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
