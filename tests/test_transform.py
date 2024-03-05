import pathlib
import sys
import os

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

import pytest

from src.csv_cleaner.transform import cast_to_int, concat

def test_cast_transform():
	assert cast_to_int('1') == 1

def test_cast_transform_no_multiple_values():
	with pytest.raises(Exception):
		assert cast_to_int(['1', '2']) == 1