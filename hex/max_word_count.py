import argparse
parser = argparse.ArgumentParser(description='Give the words and the center word')
parser.add_argument('--letters','-l', type=str, dest='letters',required=True)
parser.add_argument('--center','-c', type=str,dest='center',required=True)
args = parser.parse_args()
letters = set(args.letters)
center = args.center
words = []
with open('dictionary.txt', 'r') as f:
 for word in f.readlines():
   word_set = set(word.rstrip('\n'))
   if center in word_set and word_set.issubset(letters) and len(word)>=4:
     words.append(word.rstrip('\n'))
points = [1 if len(word) == 4 else len(word) + 1 for word in words]
longest_length = len(max(words,key=len))
longest_words = [word for word in words if len(word) == longest_length]
longest_words_str = ', '.join(longest_words)
all_letters_words = [word for word in words if len(set(word)) == len(letters)]
print(f'There are {len(words)} words.')
print(f'The maximum score is {sum(points)}.')
print(f'The maximum word length is {longest_length}.')
# print(f'The longest words are: {longest_words_str}.')
print(f'{len(all_letters_words)} words use all the letters.')
# print(all_letters_words)
with open('valid_words.txt','w+') as f:
  for word in words:
    f.write(f'{word}\n')