# numbers = [1,2,4,5,6,7,234]
# result = []
def get_even_list(numbs):
    result = []
    for n in numbs:
        if n %2 == 0:
            result.append(n)
    return result

even_list = get_even_list([1, 2, 5, -10, 9, 6])
print(get_even_list(even_list))
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")