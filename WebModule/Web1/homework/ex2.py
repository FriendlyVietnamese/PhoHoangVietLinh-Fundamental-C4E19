from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/bmi/<w>/<h>')
def bmi(w,h):
    BMI = float(w)/(float(h)/100)**2
    if BMI < 16:
        cmt = "Severely underweight"
    elif  16 <= BMI < 18.5:
        cmt = "Underweight"
    elif 18.5 <= BMI < 25:
        cmt = "Nice body"
    elif 25 <= BMI < 30:
        cmt = "Béo!"
    else:
        cmt = "Béo vãi l =))"
    return "Chỉ số BMI của bạn là {0}. {1} ".format(round(BMI,1), cmt)
    
    
    

if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 