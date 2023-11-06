from flask import Flask, request
from news import getNewsHeadline
from openAI import getRhyme
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/rhyme-headline', methods = ["POST"])
def rhymeTheTitle():
    try:
        headLine = getNewsHeadline(request.form['url'])
        print(headLine)
        text = getRhyme(headLine)
        return text
    except Exception as e:
        print("main=>", e)

if __name__ == '__main__':
    app.run(debug=True)
