import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.csv import load_csv, write_csv

def test_load_csv():
	# Test that you can load a csv, and that it has the correct amount of rows
	data = load_csv('tests/test_data/test_data_1.csv')
	# breakpoint()
	assert (len(list(data))) == 2

def test_write_csv():
	# Test that you can write to a csv

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
	data = list(data)
	write_csv('tests/test_data/test_data_1_output.csv', data)
	written_data = load_csv('tests/test_data/test_data_1_output.csv')
	assert data == list(written_data)

def test_write_csv_with_append():
	# Test that you can write to a csv, and it won't overwrite previous data

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
	data = list(data)
	write_csv('tests/test_data/test_data_1_output_appended.csv', data)
	write_csv('tests/test_data/test_data_1_output_appended.csv', data, existing=True)
	written_data = load_csv('tests/test_data/test_data_1_output_appended.csv')
	assert len(list(written_data)) ==  4