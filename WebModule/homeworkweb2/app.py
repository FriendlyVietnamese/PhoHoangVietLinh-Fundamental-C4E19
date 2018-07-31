
from flask import Flask, render_template
from mlab import connect
from models.customers import Customers
app = Flask(__name__)
connect()
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/customers")
def customers():
    customers = Customers.objects()
    return render_template("customers.html",customers = customers)

@app.route("/customers/jqk")
def jqk():
    customers = Customers.objects()
    return render_template("jqk.html", customers= customers)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 