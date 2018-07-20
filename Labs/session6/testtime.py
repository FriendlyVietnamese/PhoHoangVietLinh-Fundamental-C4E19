import datetime
import time
#lấy mốc từ bắt đầu ngày 1
#tính số giây hiện tại của ngày 1
now = datetime.datetime.now() 
current_second = now.day*86400 + now.hour*3600 + now.minute*60 + now.second
# tính tổng số giây của của 7a.m ngày hôm sau
alarm = (now.day+1)*86400 + 7*3600
# trừ đi ra thời gian hẹn giờ rồi dùng sleep() để delay.
second_to_alarm = alarm - current_second
# print(second_to_alarm)
time.sleep(second_to_alarm)