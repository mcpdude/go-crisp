import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.csv import load_csv, write_csv

def test_load_csv():
	data = load_csv('tests/test_data/test_data_1.csv')
	# breakpoint()
	assert (len(data)) == 2

def test_write_csv():
	# remove test files, if any
	try:
		os.remove('tests/test_data/test_data_1_output.csv')
	except FileNotFoundError:
		# if there's a failure with this test, or if it's never been run before, 
		# you're not going to have a file to remove
		pass
	except Exception as e:
		raise e

	data = load_csv('tests/test_data/test_data_1.csv')
	write_csv('tests/test_data/test_data_1_output.csv', data)
	written_data = load_csv('tests/test_data/test_data_1_output.csv')
	assert data == written_data

def test_write_csv_with_append():
	# remove test files, if any
	try:
		os.remove('tests/test_data/test_data_1_output.csv')
	except FileNotFoundError:
		# if there's a failure with this test, or if it's never been run before, 
		# you're not going to have a file to remove
		pass
	except Exception as e:
		raise e

	data = load_csv('tests/test_data/test_data_1.csv')
	write_csv('tests/test_data/test_data_1_output_appended.csv', data)
	write_csv('tests/test_data/test_data_1_output_appended.csv', data, existing=True)
	written_data = load_csv('tests/test_data/test_data_1_output_appended.csv')
	assert len(written_data) ==  4