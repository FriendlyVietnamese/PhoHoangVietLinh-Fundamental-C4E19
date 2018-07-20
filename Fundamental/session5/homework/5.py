price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
print(*price.keys())
find = input("Name a fruit: ")

if find in price:
    print("{0}:\nPrice: ${1}\nStock: {2}".format(find,price.values(find),stock.values(find)))

