from utils import flattener

def test_flattener():
    nested_list = [1, [2, 3], 4, [5], 6]
    assert flattener(nested_list) == [1, 2, 3, 4, 5, 6]
