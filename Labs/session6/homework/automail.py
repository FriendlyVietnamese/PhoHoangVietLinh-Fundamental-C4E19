import time
import datetime
from gmail import GMail, Message
gmail = GMail('Việt Linh<viet.ling1@gmail.com>','Vietlinh1508')
html_content =  """<p style="text-align: center;">Hề lố ma dờ fuck cơ</p>"""
msg = Message("Xin chào",
                to="kupposkai.o6200@gmail.com",
                html=html_content)
gmail.send(msg)