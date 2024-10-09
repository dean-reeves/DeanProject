# func_py_capitalize_each_word.py
def func_py_capitalize_each_word(sentence):
    return " ".join([word.capitalize() for word in sentence.split()])
