#để lấy data
from models.service import Service
import mlab
id_to_find = '5b5e01b82424e60d64caab10'
mlab.connect()
#lấy ra tất cả các object trong collection Service =>list
service = Service.objects.with_id(id_to_find)
if service is not None:
    
    print(service.to_mongo())
    service.update(set__name= "Hà")
    service.reload()
    print(service.to_mongo())
else:
    print("not found")    
##in tất cả các thông tin





#################DELETE
# if service is not None:
#     service.delete()
#     print("Deleted")
# else:
#     print("not found")

    # pass()
# first_service = all_service[0]
# print(first_service["name"])