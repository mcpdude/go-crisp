from datetime import datetime

def cast_to_int(input_value):
	""" This function takes a single input value and casts it to integer"""
	return int(input_value)

def cast_to_datetime(input_value, datetime_format=None):
	""" This function takes a single input value and casts it to datetime, given a format string"""
	return datetime.strptime(input_value, datetime_format)

def cast_to_str(input_value):
	""" This function takes a single input value and casts it to string"""

	return str(input_value)

def casing(input_value, casing):
	""" This function takes a single input value and converts it to the correct casing"""
	if casing == 'proper':
		output_value = input_value.title()
	elif casing == 'lower':
		output_value = input_value.lower()
	elif casing == 'upper':
		output_value = input_value.upper()
	else:
		raise f"Unable to handle the casing request: {casing}"
	return output_value

def concat(input_values, concat_value=''):
	return concat_value.join(input_values)

def constant(constant_value):
	return constant_value