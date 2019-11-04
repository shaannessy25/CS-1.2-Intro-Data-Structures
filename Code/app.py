from flask import Flask, render_template
from histogram import *
from sample import *


app = Flask(__name__)


@app.route('/')
def index():
    words = book('book.txt')
    histogram_words = histogram(words)
    sentence = prob_word(10, len(words), histogram_words)
    return sentence