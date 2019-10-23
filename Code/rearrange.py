import random
import sys




def rearrange(word_list):
    ''' Takes in a list of words, shuffles them, and then returns the word list '''

    random.shuffle(word_list)
    return word_list




if __name__ == '__main__':
    word_list = sys.argv[1:]
    rearrange(word_list)
    print(word_list)