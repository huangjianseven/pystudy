from collections import defaultdict

str = input("Please input a string:")

str = str.lower()

chars = defaultdict(int)

for char in str:
    chars[char] += 1

new_chars = sorted(chars.items(),key=lambda d:d[1], reverse=True)

for abc in new_chars:
    print("{}, {}".format(abc[0],abc[1]))