from urllib.request import urlopen
#1. get webpage
url = ' http://dantri.com.vn/'
#mã hóa (decode) về utf-8
data = urlopen(url).read() .decode('utf-8')
#save thành 1 file trong máy, dưới dạng open("tên file","dạng sử dụng")(W-rite, R-ead)
# f = open("dantri.html","wb")
# f.write(data)
# f.close

#2. extract ROI (region of interest))
#3. extract information

#4. save data to excel