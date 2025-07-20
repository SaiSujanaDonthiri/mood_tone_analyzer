from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    emoji = ""
    text = ""

    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.2:
            result = "😊 Happy"
            emoji = "😄"
        elif polarity < -0.2:
            result = "😢 Sad"
            emoji = "😢"
        else:
            result = "😐 Neutral"
            emoji = "😐"

    return render_template('index.html', result=result, emoji=emoji, text=text)

if __name__ == '__main__':
    app.run(debug=True)