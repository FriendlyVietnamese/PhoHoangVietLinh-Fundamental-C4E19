#video link youtube, title views thumb  youtube id
from flask import *
import mlab
from models.videos import Video
from youtube_dl import YoutubeDL
app = Flask(__name__)
mlab.connect()

##session require secret key
app.secret_key = "132465"
#
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = request.form
        user = form["user"]
        password = form["password"]
        if user == "admin" and password == "admin":
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            return "Sai tên đăng nhập hoặc mật khẩu"
@app.route("/logout")
def logout():
    del session["logged_in"]
    ##redirect(url_for("function"))
    return redirect(url_for("index"))

@app.route("/admin", methods = ["POST","GET"])
def admin():
    if "logged_in" in session:
        if request.method =="GET":
            videos = Video.objects()
            return render_template("admin.html", videos = videos)
        else:
            form = request.form
            link = form["link"]
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download=False)
            #giờ có data của video trả về dưới dạng dict
            title = data.title
            thumbnail = data.thumbnail
            views = data.view_count
            youtube_id = data.id
            new_video = Video(
                title = title,
                link = link,
                views = views,
                youtube_id = youtube_id,
                thumbnail = thumbnail
            )
            new_video.save()
            return redirect(url_for("adm    in"))
    else:
        return "Nope!"
###
@app.route('/')
def index():
    #lấy hết thông tin video ra 
    videos = Video.objects()
    return render_template('index.html', videos = videos)
###
@app.route("/detail/<youtube_id>")
def detail(youtube_id):
        return render_template("detail.html", youtube_id = youtube_id)
###

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 