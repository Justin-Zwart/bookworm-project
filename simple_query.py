import string
from word_list import words

grid = "gnlidclcaoupouui"

letter_freq = {}
for letter in grid:
    if letter in string.ascii_lowercase:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1

word_list = []
for word in words:
    if all(word.count(letter) <= letter_freq.get(letter, 0) for letter in word):
        word_list.append(word)

word_list = sorted(word_list, key=lambda x: len(x))

[print(i) for i in word_list]
