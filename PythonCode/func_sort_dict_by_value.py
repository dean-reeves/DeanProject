# func_sort_dict_by_value.py
def func_sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

print(func_sort_dict_by_value({'a': 3, 'b': 1, 'c': 2}))
