import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

import pytest

from src.csv_cleaner.csv import load_csv, write_csv
from src.csv_cleaner.config import load_json_config, verify_config
from src.csv_cleaner.transform import do_the_transforms

@pytest.mark.parametrize("input_data", 
	['tests/test_data/test_data_1.csv',
	 'tests/test_data/test_data_2.csv',
	 'tests/test_data/test_data_3.csv'])
def test_e2e(input_data):
	# load config
	config = load_json_config('tests/test_data/test_data_1_config.json')
	verified_config = verify_config(config)

	# load CSV
	data = load_csv(input_data)

	bad_rows = []
	good_rows = []
	for row in data:
		for input_column in verified_config['input']:
			pass
		# create transformed data

		good, row = do_the_transforms(row, verified_config['transforms'])

		if good:

			# select down to requested rows
			output_row = {}

			for output in verified_config['output']['columns']:
				output_row[output['name']] = row[output['input_column']]

			good_rows.append(output_row)
		else:
			bad_rows.append(row)

	if good_rows:
		write_csv(f'{input_data}_good_rows_out.csv', good_rows)
	if bad_rows:
		write_csv(f'{input_data}_bad_rows_out.csv', bad_rows)
