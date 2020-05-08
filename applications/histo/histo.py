import re

def histo():
  with open('robin.txt') as f:
    words = f.read()

  words = words.lower().split()

  words = [re.sub('\W', '', word) for word in words]

  word_count = dict()

  for word in words:
    if word_count.get(word):
      word_count[word] += 1
    else:
      word_count[word] = 1


  words_tuple = list(word_count.items())

  words_tuple.sort(key=lambda k: (-k[1], k[0]))

  longest_word = max([len(word[0]) for word in words_tuple]) + 2

  for word in words_tuple:
    print(word[0].ljust(longest_word), word[1]*'#')


histo()