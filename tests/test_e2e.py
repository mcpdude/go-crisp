import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.csv import load_csv, write_csv
from src.csv_cleaner.config import load_json_config, verify_config
from src.csv_cleaner.transform import cast_to_int, cast_to_datetime, cast_to_str, concat, constant, casing

def test_e2e():
	# load config
	config = load_json_config('tests/test_data/test_data_1_config.json')
	verified_config = verify_config(config)

	# load CSV
	data = load_csv('tests/test_data/test_data_1.csv')



	# apply transforms
	# verify input columns 
	bad_rows = []
	good_rows = []
	for row in data:
		for input_column in verified_config['input']:
			pass
		# create transformed data
		for transform in verified_config['transforms']:
			if transform['type'] == 'cast_int':
				row[transform['output_column_name']] = cast_to_int(
						row[transform['input_column']])

			elif transform['type'] == 'cast_datetime':
				row[transform['output_column_name']] = cast_to_datetime(
						row[transform['input_column']], transform['datetime_format'])

			elif transform['type'] == 'cast_str':
				row[transform['output_column_name']] = cast_to_str(
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

		# select down to requested rows
		output_row = {}

		for output in verified_config['output']['columns']:
			output_row[output['name']] = row[output['input_column']]

		good_rows.append(output_row)

	print(good_rows)
