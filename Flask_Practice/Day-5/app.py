from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/report/<int:score>")
def report(score):
    return render_template('report.html',score=score)



@app.route('/result', methods=['POST', 'GET'])
def result():
    total = 0
    if request.method == 'POST':
        data = request.form
        Bangla = float(data["Bangla"])
        English = float(data["English"])
        Math = float(data["Math"])
        total = int(Bangla + English + Math)
        return redirect(url_for("report", score=total))


if __name__ == '__main__':
    app.run(debug=True)