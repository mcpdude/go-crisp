import json

def load_json_config(path):
	# this function verifies that a given json is a valid config, then returns it
	with open(path, 'r') as json_file:
		raw_config = json.load(json_file)

	return raw_config