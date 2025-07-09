"""
test_mathematics.py
"""

import pytest

from src.mathematics import sum_numbers


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ([10, 20, 30], 60),
        ([0, 0, 0], 0),
        ([-1, -2, -3], -6),
        ([1.5, 2.5, 3.5], 7.5),
    ],
)
def test_sum_numbers(input_data, expected):
    """Test the sum_numbers function."""
    assert sum_numbers(input_data) == expected
