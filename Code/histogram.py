import sys
import re



def book(source_text):
    '''Opens text file and arranges words into a readable list '''    
    #Opens text file
    with open (source_text, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    return scrubbed_words.split(" ")


def histogram_dict(source_text):
    '''Takes text argument and returns a histogram data structure in a dictionary form'''
    histogram = {}
    words = book(source_text) 
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram

def histogram_list(source_text):
    '''Takes text argument and returns a histogram data structure in a list form'''
    words = book(source_text)
    histogram = []
    for word in words:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else: histogram.append([word, 1])
    return histogram

def histogram_tuples(source_text):
    '''Takes text argument and returns a histogram data structure in a tuples form '''
    words = histogram_list(source_text)
    histogram = []

    for item in words:
        histogram.append(tuple(item))

    return histogram



def unique_words(source_text):
    '''Takes a histogram argument and returns the total count of unique words in the histogram '''
    histogram = {}

    words = book(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else: 
            histogram[word] = 1
    print(len(histogram))

def frequency(search, source_text):
    '''Takes a word and histogram argument and returns the number of times t '''
    histogram = {}
    words = book(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else: 
            histogram[word] = 1
    print (histogram.get(search, 0))


if __name__ == '__main__':

    source_text = 'book.txt'

    histogram_dict(source_text)
    unique_words(source_text)
    frequency('and', source_text)


