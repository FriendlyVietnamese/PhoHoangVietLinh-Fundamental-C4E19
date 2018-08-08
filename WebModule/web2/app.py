#app --> mongoengine(trung gian) --> mlab   
#b1: fapp để ra Flash
#b2: tạo 1 file mlab để kết nối với database, sử dụng mongoengine
#b3: set up các thứ trong app.
#3.1 render file html để hiển thị lên page
#3.2 cung cấp các thông tin cho các biến jinja trong file html
from flask import *
import mlab
from models.service import Service

app = Flask(__name__)
mlab.connect()
#Trang chủ index
@app.route('/')
def index():
    return render_template('index.html')

#Search
@app.route("/search/<gender>")
def search(gender):
#từ thằng Service(), dùng hàm objects() để lấy tất cả thông tin cần thiết
    all_service = Service.objects(gender = gender, yob__lte = 1998)
    return render_template("search.html",
                all_service=all_service,
                )

#Admin
@app.route("/admin", methods = ["POST","GET"])
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)

#delete id
@app.route("/delete/<service_id>")
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service_id is not None:
        service.delete()
##redirect(url_for("tên_function"))
        return redirect(url_for("admin"))
    else:
        return "Oop! Có gì đó sai sai. Thử reload page xem=))"

##tạo service
@app.route("/new-service", methods =["GET","POST"])
def new_service():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
##lỗi 400: lấy sai tên biến, check lại đồng trên hoặc new_service.html
        new_service = Service(
            name = name,
            yob = yob,
            height = height
        )
        detail = detail(
            image = image,
            name = name ,
            yob = yob,
            height = height,
            phone = phone,
            address = address,
            info = info,
            describe = describe
        )
    new_service.save()
    detail.save()
    return redirect(url_for("admin"))
##
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


 