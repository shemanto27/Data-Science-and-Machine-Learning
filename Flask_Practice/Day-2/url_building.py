from flask import Flask, redirect, url_for
import time
import logging

app = Flask(__name__)

@app.route("/passed/<name>/<int:score>")
def passed(name, score):
    return f"Congrats {name},you have passed! Your score is {score}"

@app.route("/failed/<name>/<int:score>")
def failed(name, score):
    return f"Sorry {name}, you have failed! Your score is: {score}"

@app.route('/score/<person>/<int:num>')
def score_display(person, num):
    if num >= 40:
        time.sleep(1)
        return redirect(url_for("passed", name=person, score=num))
    elif num <40:
        time.sleep(1) 
        return redirect(url_for("failed", name=person, score=num))


if __name__ == '__main__':
    app.run(debug=True)