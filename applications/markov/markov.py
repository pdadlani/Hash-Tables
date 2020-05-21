import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# analyze which words can follow other words

words = words.split()

# instantiate a words dict
words_dict = dict()

# iterate through each word in words
for i in range(len(words)-1):
    curr_word = words[i]
    next_word = words[i+1]
    # if the word aka key exists in the dict
    if words_dict.get(curr_word):
        # add the next word to the list 'value'
        words_dict[curr_word].append(next_word)
    # else create a new key entry, with the next word as an item in a list for the 'value'
    else:
        words_dict[curr_word] = []
        words_dict[curr_word].append(next_word)


# construct 5 random sentences
# start words, choose at random.
start_words = [word for word in words_dict.keys() if word[0].isupper() or word[0] == '"']

punct = ['.', '!', '?', '!"', '?"', '."']

end_words = [word for word in words_dict.keys() if word[-1:] in punct or word[-2:] in punct]

# for 5 times
for i in range(5):
    # create a new string
    # append one random start word
    word = random.choice(start_words)
    # print word
    print(word)
    # find more words until you reach and end word
    while word not in end_words:
        word = random.choice(words_dict[word])
        print(word, end=" ")
    print('\n')
