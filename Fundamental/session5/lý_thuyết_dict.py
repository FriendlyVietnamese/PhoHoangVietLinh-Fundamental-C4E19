#dictionary {}
#lưu thông tin theo cặp key:value.
#  giống như từ điển, từ và nghĩa của từ

person = {
    "name":"Quân",
    "age":22,
    "ex":2,
    "favs":["Ping ping","PES"]
}
# print(person)
####CÁC CÁCH ĐỂ IN RA ITEM TRONG DIC
##cách 1:
# key = "name"
# if key in person:
#     print(person[key])
# else:
#     print("Not found!")


##cách 2
# print(person,"\n")
# for key in person.keys():
#     print(key, end ="\t")
# for key,value in person.items():
#     print("{0}: {1}".format(key,value))
##cách 3
# n person.values():for value i
#     print(value, end = "\n ")


##update
person['name'] = "Quân Kun"
print(person)

##delete items
del person["ex"]
print(person)