from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict


app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    sentence_size = 20
    sentence_list = list()
    text = 'book.txt'
    for i in range(0, sentence_size):
        sentence_list.append(main_sample(text))
    sentence_str = " ".join(sentence_list)
    return render_template('base.html', sentence=sentence_str)


if __name__ == '__main__':
    app.run(debug=True)