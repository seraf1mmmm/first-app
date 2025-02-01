words_list = []
a = 0
b = int(input("How many? "))


if b > 0:
    while a < b:
        words = input("Print a word ")
        words_list.append(words)
        a += 1
else:
    print("list can't be 0")

print(words_list)