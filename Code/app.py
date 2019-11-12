from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# import os

app = Flask(__name__)

# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/tweet-generator-sh')
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
# tweet = db['tweet']

@app.route('/')
def index():
    """Return Homepage"""
    text = 'book.txt'
    sentence = main_sample(text)
    return render_template('base.html', sentence=sentence)
    # source_text = 'book.txt'
    # tweet_list = {
    #     'tweet' : main_sample(source_text)
    # }

    # tweet_id = tweet.insert.one(tweet_list).inserted_id
    # tweet_text = tweet.find.one({'_id': ObjectId(tweet_id)})['tweet']
    # return render_template('base.html', tweet_id=tweet_id, tweet_text=tweet_text)


    




# histogram = histogram_dict(text)



if __name__ == '__main__':
    app.run(debug=True)



# host='0.0.0.0', port=os.environ.get('PORT', 5000)




# git subtree push --prefix Code heroku master