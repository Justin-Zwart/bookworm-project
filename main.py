import string
from word_list import words

valid_words = {}

#### DO 01-07B NEXT

# Loop through each image in the directory
with open("grids", "r") as grids:
    for grid in grids.readlines():
        print(grid.strip("\n"))
        # Count the frequency of each letter in the result string
        letter_freq = {}
        for letter in grid:
            if letter in string.ascii_lowercase:
                letter_freq[letter] = letter_freq.get(letter, 0) + 1

        # Find all words that can be formed using the letters in the result string
        for word in words:
            if all(word.count(letter) <= letter_freq.get(letter, 0) for letter in word):
                if len(word) not in valid_words:
                    valid_words[len(word)] = {}
                valid_words[len(word)][word] = valid_words[len(word)].get(word, 0) + 1

        # Write the results to separate files for each word length
        for length in range(3, 17):
            if length in valid_words:
                with open(f'results/output_{length}.txt', 'w') as f:
                    sorted_words = sorted(valid_words[length].items(), key=lambda x: -x[1])
                    for word, count in sorted_words:
                        f.write(f'{word} {count}\n')
