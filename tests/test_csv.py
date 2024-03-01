import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.csv import load_csv

def test_load_csv():
	data = load_csv('tests/test_data/test_data_1.csv')
	# breakpoint()
	assert (len(data)) == 2

def write_csv():
	pass