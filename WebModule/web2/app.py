#app --> mongoengine(trung gian) --> mlab   
#b1: fapp để ra Flash
#b2: tạo 1 file mlab để kết nối với database, sử dụng mongoengine
#b3: set up các thứ trong app.
#3.1 render file html để hiển thị lên page
#3.2 cung cấp các thông tin cho các biến jinja trong file html
from flask import Flask, render_template
import mlab
from models.service import Service
app = Flask(__name__)
mlab.connect()
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/search/<gender>")
def search(gender):
#từ thằng Service(), dùng hàm objects() để lấy tất cả thông tin cần thiết
    all_service = Service.objects(gender = gender, yob__lte = 1998)
    return render_template("search.html",
                all_service=all_service,
                )

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 