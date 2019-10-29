import random
import sys



def list_random_words(num):
    '''Opens dictionary file and picks random words based on user input '''
    dictionary = open('/usr/share/dict/words', 'r')                 #opens the stored dictionary file
    words = dictionary.read().split()                               #takes the words in the file and adds them to a readable list
    sentence = [random.choice(words) for _ in range(0, int(num))]   #takes a certain number (terminal input) of random words from the list
    dictionary.close()                                              #closes dictionary file
    return ' '.join(sentence) + '.'                                 #takes words and lists them in a string

if len(sys.argv) > 1:
    print(list_random_words(sys.argv[1]))

