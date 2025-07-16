"""
Module: mathematics.py
Description:
    This module provides mathematical functions for various calculations.
"""

from typing import List, Union


def sum_numbers(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Sums a list of numbers.

    Parameters
    ----------
    numbers : List[Union[int, float]]
        A list of numbers (int or float) to be summed.

    Returns
    -------
    Union[int, float]
        The sum of the numbers in the list.
    """

    return sum(numbers)
