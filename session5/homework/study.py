sentence = input("Nhập 1 câu dài bất kì: \n")
counts = {}
for letter in sentence:
    if letter == " ":
        pass
    else:
        counts[letter] = counts.get(letter,0) + 1
print(counts)