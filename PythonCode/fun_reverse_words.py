# fun_reverse_words.py
def fun_reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

print(fun_reverse_words('Hello World'))
