"""
Helper functions
"""

def flattener(nested_list):
    """Takes a nested list and flattens it"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flattener(item))
        else:
            result.append(item)
    return result
