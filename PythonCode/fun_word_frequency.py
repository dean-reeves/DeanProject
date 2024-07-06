# fun_word_frequency.py
def word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower().strip('.,!?"\'')
        freq[word] = freq.get(word, 0) + 1
    return freq

file_path = "example.txt"
print(word_frequency(file_path))
