import MapReduce
import sys

"""
DNA
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: sequence id
	# value: nucleotides
	key = record[0]
	value = record[1][:-10]
	mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence document_ids
	mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
