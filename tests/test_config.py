import pathlib
import sys
import os
import pytest

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from src.csv_cleaner.config import load_json_config, verify_config

def test_load_config():
	# Test that you can load a config from json
	config = load_json_config('tests/test_data/test_data_1_config.json')
	assert 'input' in config.keys()
	assert 'transforms' in config.keys()
	assert 'output' in config.keys()

# TODO: would be good to use a fixture here to avoid loading twice
def test_verify_config():
	# Test that you can load a config from json, then verify it
	config = load_json_config('tests/test_data/test_data_1_config.json')
	verified_config = verify_config(config)
	assert type(verified_config) == dict

def test_verify_bad_config():
	# Test that you can load a config from json, then verify it, and that the verification catches a bad config
	config = load_json_config('tests/test_data/test_data_1_bad_config.json')
	with pytest.raises(Exception):
		assert verified_config == verify_config(config)

