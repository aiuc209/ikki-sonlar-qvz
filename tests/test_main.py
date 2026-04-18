import pytest

def sum_pairs(a, b):
    return [x + y for x, y in zip(a, b)]

def test_sum_pairs():
    assert sum_pairs([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def test_sum_pairs_unequal_length():
    with pytest.raises(ValueError):
        sum_pairs([1, 2, 3], [4, 5])

def test_sum_pairs_empty_lists():
    assert sum_pairs([], []) == []

def test_sum_pairs_negative_numbers():
    assert sum_pairs([-1, -2, -3], [4, 5, 6]) == [3, 3, 3]

def test_sum_pairs_floats():
    assert sum_pairs([1.5, 2.5, 3.5], [4.5, 5.5, 6.5]) == [6.0, 8.0, 10.0]
