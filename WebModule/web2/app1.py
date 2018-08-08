from flask import *
from models.service import Service
import mlab
app = Flask(__name__)
mlab.connect()

#Trang chủ
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)


@app.route("/delete/<service_id>")
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service_id is not None:
        service.delete()
##redirect(url_for("tên_function"))
        return redirect(url_for("admin"))
    else:
        return "Oop! Có gì đó sai sai. Thử reload page xem=))"
#xem các người đã có
@app.route("/search")
def search():
    all_service = Service.objects()
    return render_template("search.html", all_service = all_service) 

@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template ('detail.html', service = service)
  

@app.route("/new-service", methods =["GET","POST"])
def new_service():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
        phone = form["phone"]
        address = form["address"]
        info = form["info"]
        describe = form["describe"]
##lỗi 400: lấy sai tên biến, check lại dòng trên hoặc new_service.html
        new_service = Service(
            # image = image,
            name = name ,
            yob = yob,
            height = height,
            phone = phone,
            address = address,
            info = info,
            describe = describe
        )
    new_service.save()
    return redirect(url_for("admin"))

@app.route("/update/<service_id>", methods = ["GET","POST"])
def update(service_id):
    
    service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template("update.html", service = service)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        height = form["height"]
        phone = form["phone"]
        address = form["address"]
        info = form["info"]
        describe = form["describe"]
        
    
    service.update(
        set__name = name,
        set__yob = yob,
        set__height = height,
        set__phone =phone,
        set__address = address,
        set__info = info,
        set__describe = describe
        )
    return redirect(url_for("admin"))
    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 