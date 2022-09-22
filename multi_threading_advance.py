# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_number(start,end):
    # function to print cube of given num
    for num in range(start,end):
        print(num)



if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_number, args=(11,18))
    t2 = threading.Thread(target=print_number, args=(1,8))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    #t1.join()
    # wait until thread 2 is completely executed
    #t2.join()

    print_number(21,28)

    # both threads completely executed
    print("Done!")
