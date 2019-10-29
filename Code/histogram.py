import sys
import re

source_text = 'book.txt'

def book(source_text):
    '''Opens text file and arranges words into a readable list '''    
    #Opens text file
    with open (source_text, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    return scrubbed_words.split(" ")


def histogram(source_text):
    '''Takes text argument and returns a histogram data structure '''
    histogram = {}
    words = book(source_text) 
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1 
    return histogram

def histogram_list(source_text):
    words = book(source_text)
    histogram = []

    for word in words:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else: histogram.append([word, 1])
    return histogram



def unique_words():
    '''Takes a histogram argument and returns the total count of unique words in the histogram '''
    pass

def frequency():
    '''Takes a word and histogram argument and returns the number of times t '''
    pass



print(histogram_list(source_text))
     
    



















# text = ['one', 'fish', 'two', 'red', 'fish', 'blue', 'fish']