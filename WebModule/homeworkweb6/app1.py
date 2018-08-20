from flask import *
from models.service import *
import mlab
import time
app = Flask(__name__)
mlab.connect()
app.secret_key = "000000"
#Trang chủ
@app.route('/')
def index():
    return render_template('index.html')
#Page Admin
@app.route("/admin", methods = ["GET", "POST"])
def admin():
    if request.method ==  "GET":
        return render_template("admin_login.html")
    elif request.method == "POST":
        form = request.form
        user = form['user']
        password = form['password']
        if user == "admin" :
            if password == "admin":
                session["admin"] = True
                return render_template("admin.html", all_service = all_service)
            else:
                return "Sai mật khẩu, vui lòng back lại"  
            
        else:
            return "bạn đ phải admin! Vui lòng back lại"
       
##DELETE SERVICE
@app.route("/delete/<service_id>")
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service_id is not None:
        service.delete()
##redirect(url_for("tên_function"))
        return redirect(url_for("admin"))
    else:
        return "Oop! Có gì đó sai sai. Thử reload page xem=))"
#xem các Service đã có
@app.route("/search")
def search():
    all_service = Service.objects()
    return render_template("search.html", all_service = all_service) 


  
##Create Service
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
##Update service
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
##Sign-Up   
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return  render_template("signup.html")
    elif request.method == "POST":
        form = request.form
        new_user = User(
            name = form["name"],
            email = form["email"],
            user = form["user"],
            password = form["password"]
        )
        new_user.save()
    return redirect(url_for('search'))
##LOGIN
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        user = form['user']
        password = form['password']
        user_data = User.objects(user = user, password = password)
        if len(user_data) == 1:
            session['logged_in'] = True
            session['user_id'] = str(user_data[0].id)
            return redirect (url_for('index'))
        else:
            return "Sai tên đăng nhập hoặc mật khẩu"
##DETAIL
@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    if "logged_in" not in session:
        return redirect(url_for("login"))
    elif "logged_in" in session:
        return render_template ('detail.html', service = service)

##ORDER
@app.route("/order/<service_id>")
def order(service_id):
    # user = User.objects(service_id)
    if "logged_in" in session:
        new_order = Order(
            service_id = service_id,
            user_id = session["user_id"],
            time = datetime.datetime.now,
            is_accepted = False    
        )
        new_order.save()
        return "Đã gửi yêu cầu"
    else:
        return "Bạn chưa đăng nhập"

@app.route("/logout")
def logout():
    if "logged_in" in session:
        del session["logged_in"]
        del session["user_id"]
    elif "admin" in session:
        del session["admin"]
    else:
        pass
    
    ##redirect(url_for("function"))
    return redirect(url_for("index"))




        


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 