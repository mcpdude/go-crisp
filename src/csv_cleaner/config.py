import json

def load_json_config(path):
	# this function verifies that a given json is a valid config, then returns it
	with open(path, 'r') as json_file:
		raw_config = json.load(json_file)

	return raw_config

def verify_config(config: dict):
	# This checks that the config has a valid schema
	assert 'input' in config.keys()
	assert 'output' in config.keys()
	
	# input tests
	assert 'expected_columns' in config['input'].keys()
	assert len(config['input']['expected_columns']) > 0
	for column in config['input']['expected_columns']:
		assert 'column_name' in column.keys()
		assert 'regex' in column.keys()

	# output tests
	assert 'columns' in config['output'].keys()
	assert len(config['output']['columns']) > 0
	for column in config['output']['columns']:
		assert 'name' in column.keys()
		assert 'type' in column.keys()
		assert 'nullable' in column.keys()
		assert 'transforms' in column.keys()

	return config