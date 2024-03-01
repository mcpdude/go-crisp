import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.config import load_json_config

def test_load_config():
	config = load_json_config('tests/test_data/test_data_1_config.json')
	assert 'input' in config.keys()
	assert 'output' in config.keys()
