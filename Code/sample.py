import random
from histogram import histogram_dict

def prob_word(histogram, count):
    '''returns a random word '''
    total = 0
    index = random.randint(1, count)

    for key, value in histogram.items():
        total += value

        if index <= total:
            return key

def main_sample(source_text):
    words = histogram_dict(source_text)
    count = sum(words.values())

    word = prob_word(words, count)
    return word

if __name__ == '__main__':
    source_text = 'book.txt'
    histogram = histogram_dict(source_text)
    print(prob_word(histogram, 21))
    