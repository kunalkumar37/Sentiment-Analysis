from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('ss1.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = flask.request.json
    text = data['text']

    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return flask.jsonify({'sentiment': sentiment, 'score': sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)