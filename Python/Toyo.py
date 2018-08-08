import urllib, cStringIO

a = cStringIO.StringIO(urllib.urlopen("https://www.google.com.vn/search?tbm=isch&q=tattoo#imgrc=ahYQM4Ri6sQVgM:").read())
img = Image.open(a)