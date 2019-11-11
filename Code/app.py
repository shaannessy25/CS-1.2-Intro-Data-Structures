from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'book.txt'
    sentence = main_sample(text)
    return render_template('base.html', sentence=sentence)

 




# histogram = histogram_dict(text)


























# from flask import Flask, render_template, request, url_for
# from histogram import book, histogram
# from sample import prob_word


# app = Flask(__name__)


# @app.route('/', methods =['GET', 'POST'])
# def index():
#     words = book('book.txt')
#     number_of_words = 20
#     histogram_words = histogram(words)

#     if request.method == 'POST':
#         number_of_words = request.form.get('word_count')
#     sentence = prob_word(number_of_words, len(words), histogram_words)
#     return render_template('base.html', sentence=sentence)



# if __name__ == '__main__':
#     app.run(debug=True)