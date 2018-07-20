#Thư viện các thứ
from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
#uri + connect database + get collection Customers
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.get_default_database()
customers = db["customers"]
customer_no = customers.find()
#đếm
counter_for_ad = db.customers.find({"ref":"ads"}).count()
counter_for_events = db.customers.find({"ref":"events"}).count()
counter_for_wom = db.customers.find({"ref":"wom"}).count()

#giờ có giá trị counter, prepare data.
labels = ["Ads","Events","Wom"] 
colors = ["red","yellow","green"]
portion = [counter_for_ad,counter_for_events,counter_for_wom]
pyplot.pie(portion,
            labels = labels,
            colors= colors)
pyplot.axis("equal")
pyplot.show()


