from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route("/<user>")
def user_infor(user):
    users = {"quan" : {
			"name" : "Nguyen Anh Quan",
			"age" : 16
    },
    "tuananh" : {
    		   "name" : "Huynh Tuan Anh",
			   "age" : 23
       }
}
    return "name: {0}. Age:{1}".format(users[user]["name"],users[user]["age"])
    # return render_template("users.html",users = users)
    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 