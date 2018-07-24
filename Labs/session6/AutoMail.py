##HẸN GIỜ ĐỂ TỰ GỬI MAIL VÀO 7H SÁNG
##Import thư viên gmail
#import thư viên random để lấy lý do ngẫu nhiên


from gmail import GMail,Message
from random import choice
import datetime
import time
#hẹn giờ để thư tự gửi
now = datetime.datetime.now() 
current_second = now.day*86400 + now.hour*3600 + now.minute*60 + now.second
# tính tổng số giây của của 7a.m ngày hôm sau
alarm = (now.day+1)*86400 + 7*3600
# trừ đi ra thời gian hẹn giờ rồi dùng sleep() để hẹn giờ.
second_to_alarm = alarm - current_second



#tạo địa chỉ người gửi bằng lệnh GMail("User,<123@xyz.com>","password")
gmail = GMail('Việt Linh<viet.ling1@gmail.com>','Vietlinh1508')
##nội dung thôi ko cần quan tâm đâu
htlm_content = """<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
    <p style="text-align: center;">Độc Lập - Tự Do - Hạnh Ph&uacute;c</p>
    <p style="text-align: center;">&nbsp;</p>
    <p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
    <p style="text-align: left;">K&iacute;nh gửi: Ng&agrave;i Huỳnh Tuấn Anh _ Giảng vi&ecirc;n lớp C4E19</p>
    <p style="text-align: left;">L&yacute; do viết đơn: Em bị {{sickness}} n&ecirc;n ko đi học được</p>
    <p>Em xin cảm ơn v&agrave; hậu tạ</p>
    """
reasons = ["kẹt chân trong toilet","mẹ giữ ở nhà","tông xe","ngã máy bay","ngu","kẹt chân trong đường ray"]
htlm_to_send = htlm_content.replace("{{sickness}}",choice(reasons))
# Nội dung tin nhắn/ dùng lệnh msg = Message
msg = Message('Đơn xin nghỉ học',
            to = "viet.ling1@gmail.com",
           
            html=htlm_to_send)
time.sleep(second_to_alarm)
gmail.send(msg)
print("Done!")

