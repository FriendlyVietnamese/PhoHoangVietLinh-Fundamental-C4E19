#để lấy data
from models.service import Service
import mlab

mlab.connect()
# http://docs.mongoengine.org/guide/querying.html#query-operators
#lấy ra tất cả các object trong collection Service =>list
all_service = Service.objects()
first_service = all_service[0]
print(first_service["name"])