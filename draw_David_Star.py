import turtle as tr
import math

i = 1
j = 1

count = int(input("Please input the count of distance:"))

tr.pendown()

while j <= count:
    tr.left(360/count)
    tr.fd(90)
    tr.right(360*2/count)
    tr.fd(90)
    j=j+1

d = 2*90*math.cos(2*math.pi/count)

while i<= count:
    tr.fd(d)
    tr.right(360/count)
    i=i+1

tr.penup()
tr.done()
