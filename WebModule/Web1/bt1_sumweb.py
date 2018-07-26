from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return ('Trang chủ')
@app.route("/sum/<int:no1>/<int:no2>")
def total(no1,no2):
    # a = int(no1) + int(no2)
    return "{0} + {1} = {2}".format(int(no1),int(no2),no1+no2)

if __name__ == '__main__':
  app.run(port = 5432,debug=True)
 