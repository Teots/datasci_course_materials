import MapReduce
import sys

"""
Relational Join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: source
	# value: order_id
	key = record[0]
	value = record[1]
	mr.emit_intermediate(value, record)

def reducer(key, list_of_values):
	# key: order_id
	# value: list of data
	line_items = []
	orders = []
	for v in list_of_values:
		if len(v) == 17:
			line_items.append(v)
		else:
			orders.append(v)
	
	for line_item in line_items:
		for order in orders:
			mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
