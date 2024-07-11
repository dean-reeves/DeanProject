# func_sort_dict_by_key.py
def func_sort_dict_by_key(d):
    return dict(sorted(d.items()))

sample_dict = {'banana': 2, 'apple': 10, 'cherry': 5}
print(func_sort_dict_by_key(sample_dict))
