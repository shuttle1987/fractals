"""
Helper functions
"""

def flattener(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flattener(item))
        else:
            result.append(item)
    return result
