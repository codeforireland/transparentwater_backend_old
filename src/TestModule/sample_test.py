"""
Tests sample functions
"""
from .sample import sample_func


def test_sample_func():
    assert sample_func(4) == 5
