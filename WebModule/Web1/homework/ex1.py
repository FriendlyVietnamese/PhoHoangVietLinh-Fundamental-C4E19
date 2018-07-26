from urllib.request import urlopen
from flask import Flask, render_template,redirect
url =  "http://techkids.vn" 
app = Flask(__name__)

@app.route("/")
def trang_chu():
        return render_template("index.html")
@app.route('/about-me')
def about_me():
    data = {
        "name":"VLinh",
        "age":"19",
        "school":"Đại học Bách Khoa Hà Lội",
        "hobbies":"Guitar, LoL, Doing nothing"
    }
    return render_template('personal_infor.html',data = data)
@app.route("/school")

def school():
    return  redirect(url)


if __name__ == '__main__':
  app.run(host= '127.0.0.1', port=5000, debug=True)
 