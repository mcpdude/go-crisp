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

	# transform tests
	assert len(config['transforms']) > 0
	for transform in config['transforms']:
		assert 'input_columns' or 'input_column' in transform.keys()
		assert 'output_column_name' in transform.keys()

	# output tests
	assert 'columns' in config['output'].keys()
	assert len(config['output']['columns']) > 0
	for column in config['output']['columns']:
		assert 'name' in column.keys()
		assert 'input_column' in column.keys()

	return config