import MapReduce
import sys

"""
Social Network
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	matrix = record[0]
	row = record[1]
	col = record[2]
	value = record[3]

	if matrix == 'a':
		for i in range(0, 5):
			mr.emit_intermediate((row, i), record)
	else:
		for i in range(0, 5):
			mr.emit_intermediate((i, col), record)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence document_ids
	total = 0
	for a in list_of_values:
		for b in list_of_values:
			if a[0] == 'a' and b[0] == 'b' and a[2] == b[1]:
				total += a[3] * b[3]

	mr.emit(key + (total, ))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
