import random
import sys



def list_random_words(num):
    dictionary = open('/usr/share/dict/words', 'r')  #opens the stored dictionary file
    words = dictionary.read().split()                # takes the words in the file and adds them to a readable list
    sentence = [random.choice(words) for _ in range(0, int(num))]
    dictionary.close()
    return ' '.join(sentence) + '.'

if len(sys.argv) > 1:
    print(list_random_words(sys.argv[1]))
