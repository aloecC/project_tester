from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, 'test') == 'test'
    assert arrs.get([1, 2, 3, 4], -1, 'test') == 'test'
    assert arrs.get([1, 2, 3, 4], 5, 'test') == 'test'
    assert arrs.get([1, 2, 3, 4], 0, 'test') == 1



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -3, -1) == [1, 2]
    assert arrs.my_slice([], -3) == []
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], None, 3) == [1, 2, 3]
