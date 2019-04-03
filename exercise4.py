from random import randint

# string_input = str(input('Type something'))
# string_arr = list(string_input)
# char_string = []

# while len(string_arr) > 0:
#     ask_string = randint(0, len(string_arr) - 1)
#     char_string.append(string_arr[ask_string])
#     string_arr.pop(ask_string)

# for i in char_string: 
#     print(i)

word = ['hello', 'ajinomoto', 'opppsi', 'anhoaseo']
ask = randint(0, len(word) -1 )
word_arr = list(word[ask])
char_word = []

while len(word_arr) > 0:
    index = randint(0, len(word_arr) - 1)
    char_word.append(word_arr[index])
    word_arr.pop(index)

for j in char_word:
    print(j)

answer = str(input('Guess what is this word'))
if answer == word[ask]:
    print('You guess right')
else:
    print('You guess wrong. The answer is ', word[ask])