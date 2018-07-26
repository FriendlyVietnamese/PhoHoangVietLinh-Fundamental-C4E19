from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<w>/<h>')
def BMI(w,h):
    chi_so = float(w)/(float(h)/100)**2
    if chi_so < 16:
        cmt = "Gầy vãi lều=))"
    elif  16 <= chi_so < 18.5:
        cmt = "Underweight"
    elif 18.5 <= chi_so < 25:
        cmt = "Người ngợm ngon đấy=))"
    elif 25 <= chi_so < 30:
        cmt = "Béo!"
    else:
        cmt = "Béo vãi l =))"
    return render_template("BMI.html", h = h , w = w, cmt = cmt , bmi = round(chi_so,2) )
    

if __name__ == '__main__':
  app.run(host= '127.0.0.1', port=8000, debug=True)
 