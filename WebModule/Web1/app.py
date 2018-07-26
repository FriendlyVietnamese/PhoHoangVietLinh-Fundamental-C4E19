##Đây là data
# #import thư viện Flask
from flask import Flask,render_template
#tạo ra 1 cái sever bằng Flash
app = Flask(__name__)

#đi đến trang chủ
@app.route('/')
def index():
    posts_data = [
        {
            "title":"Thơ con cóc",
            "content": "Chị tôi lớn tuổi hơn tôi<br>Mẹ tôi lớn tuổi hơn tôi rất nhiều<br>Ơ kìa có một chiếc diều<br>Diều mà có gió thì diều sẽ bay",
            "author": "Vilinh",
            "gender": 0

        },
        {
            "title":"Thơ con nhái",
            "content": "Chị tôi lớn tuổi hơn tôi<br>Mẹ tôi lớn tuổi hơn tôi rất nhiều<br>Ơ kìa có một chiếc diều<br>Diều mà có gió thì diều sẽ bay",
            "author": "Vilinh",
            "gender": 1
        }
        ]
    return render_template(
        "index.html",posts_data = posts_data  )
#đi đến 1 cổng
@app.route("/hello")
def hello():
    return "http://techkids.vn"

@app.route('/say_high/<name>/<age>')
def say_high(name,age):
    return ("Xin chào! Tôi là {0}, {1} tuổi. Tôi tới từ Sao Hỏa. ".format(name,age))
# def hello_1():
    # return("    Xin chào C4E19!!!!")
#khi mà file được chạy Trực Tiếp--> app.run
if __name__ == '__main__':
#debug = True --> liên tục cập nhật sever, ko cần phải tắt đi bật lại sever nữa
  app.run(debug=True)
 