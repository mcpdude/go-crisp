import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.csv import load_csv, write_csv
from src.csv_cleaner.config import load_json_config, verify_config
from src.csv_cleaner.transform import do_the_transforms

def test_e2e():
	# load config
	config = load_json_config('tests/test_data/test_data_1_config.json')
	verified_config = verify_config(config)

	# load CSV
	data = load_csv('tests/test_data/test_data_1.csv')

	bad_rows = []
	good_rows = []
	for row in data:
		for input_column in verified_config['input']:
			pass
		# create transformed data
		
		row = do_the_transforms(row, verified_config['transforms'])

		# select down to requested rows
		output_row = {}

		for output in verified_config['output']['columns']:
			output_row[output['name']] = row[output['input_column']]

		good_rows.append(output_row)

	print(good_rows)
