# Python program to illustrate the concept
# of threading
# importing the threading module

def print_number(start,end):
    # function to print cube of given num
    for num in range(start,end):
        print(num)


print_number(1,8)
print_number(11,18)

for num in range(21,28):
    print(num)

# both threads completely executed
print("Done!")
