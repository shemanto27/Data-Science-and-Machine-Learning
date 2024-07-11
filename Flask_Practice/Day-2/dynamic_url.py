from flask import Flask, redirect, url_for
import time
app = Flask(__name__)

@app.route("/passed")
def passed():
    return "Congrats,you have passed!"

@app.route("/failed")
def failed():
    return "Sorry, you have failed!"

@app.route('/score/<name>/<int:num>')
def score_display(name, num):
    if num >= 40:
        time.sleep(1)
        return redirect(url_for("passed"))
    else:
        time.sleep(1) 
        return redirect(url_for("failed"))


if __name__ == '__main__':
    app.run(debug=True)