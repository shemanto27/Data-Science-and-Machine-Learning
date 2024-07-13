from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/report/<int:score>")
def report(score):
    return render_template('report.html',total_score=score) #Pass score to the report template

# total_score before the = sign is the name of the variable that will be available in the template, and the score after the = sign is the value being passed to the template (which is the parameter received by the function)


@app.route('/result', methods=['POST', 'GET'])
def result():
    total = 0
    if request.method == 'POST':
        data = request.form
        Bangla = float(data["Bangla"])
        English = float(data["English"])
        Math = float(data["Math"])
        total = int(Bangla + English + Math)
        return redirect(url_for("report", score=total)) #Pass score to redirect call
# score=total is used to pass the total variable's value as the score parameter to the report endpoint.

if __name__ == '__main__':
    app.run(debug=True)