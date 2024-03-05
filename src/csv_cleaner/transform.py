

def caster(input_values, output_type):
	""" This function takes a single input value and casts it to a given type"""
	assert len(input_values) == 1
	input_value = input_values[0]
	if output_type == 'int':
		return int(input_value)

def concat(input_values):
	pass

def constant_value(input_values):
	pass