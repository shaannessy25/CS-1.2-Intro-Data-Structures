import random
import sys



def rearrange(words_list):
    """
    rearranges given words from the user
    """
    for i, word in enumerate(words_list):
        random_index = random.randint(0, len(words_list) - 1)
        words_list[i] = words_list[random_index]
        words_list[random_index] = word
    return words_list
    # random.shuffle(word_list)
    # return word_list




