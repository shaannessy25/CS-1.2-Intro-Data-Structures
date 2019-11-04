import random
from histogram import *

def get_count(histogram):
    '''Counts and sums the values of histogram'''
    count = 0
    for key, value in histogram.items():
        count += value
    return count

def prob_word(histogram, count):
    ''' '''
    total = 0
    index = random.randint(1, count)

    for key, value in histogram.items():
        total += value

        if index <= total:
            return key

def main_sample(source_text):
    words = histogram(source_text)
    count = get_count(words)

    word = prob_word(words, count)
    print (word)

if __name__ == '__main__':
    source_text = 'book.txt'
    main_sample(source_text)
    