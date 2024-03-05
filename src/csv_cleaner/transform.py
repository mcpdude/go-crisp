from datetime import datetime
from decimal import Decimal

def cast_to_int(input_value):
	""" This function takes a single input value and casts it to integer"""
	return int(input_value)

def cast_to_datetime(input_value, datetime_format=None):
	""" This function takes a single input value and casts it to datetime, given a format string"""
	return datetime.strptime(input_value, datetime_format)

def cast_to_str(input_value):
	""" This function takes a single input value and casts it to string"""

	return str(input_value)

def cast_to_decimal(input_value):
	""" This function takes a single input value and casts it to decimal"""
	input_value = input_value.replace(',', '')
	return Decimal(input_value)


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
	""" This function takes input values and concatenates them with a optional concat value"""
	return concat_value.join(input_values)

def constant(constant_value):
	""" This function returns a constant value given. Yes, it is superfluous."""
	return constant_value

def do_the_transforms(row, transforms):
	for transform in transforms:
		if transform['type'] == 'cast_int':
			row[transform['output_column_name']] = cast_to_int(
					row[transform['input_column']])

		elif transform['type'] == 'cast_datetime':
			row[transform['output_column_name']] = cast_to_datetime(
					row[transform['input_column']], transform['datetime_format'])

		elif transform['type'] == 'cast_str':
			row[transform['output_column_name']] = cast_to_str(
					row[transform['input_column']])

		elif transform['type'] == 'cast_decimal':
			row[transform['output_column_name']] = cast_to_decimal(
					row[transform['input_column']])

		elif transform['type'] == 'casing':
			row[transform['output_column_name']] = casing(
					row[transform['input_column']], transform['casing_choice'])

		elif transform['type'] == 'concat':
			# don't like this
			input_values = [row[key] for key in transform['input_columns']]

			if transform['concat_value']:
				row[transform['output_column_name']] = concat(
					input_values, transform['concat_value'])
			else:
				row[transform['output_column_name']] = concat(
					input_values)

		elif transform['type'] == 'constant':
			# try:
			row[transform['output_column_name']] = constant(
					transform['constant_value'])
		else:
			print(f"Transform of type: {transform['type']} not recognized.")

	return row