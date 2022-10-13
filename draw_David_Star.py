import turtle as tr
import math

i = 1
j = 1

tr.pendown()

while j <= 5:
    tr.left(360/5)
    tr.fd(90)
    tr.right(360/2.5)
    tr.fd(90)
    j=j+1

d = 2*90*math.cos(2*math.pi/5)

while i<= 5:
    tr.fd(d)
    tr.right(365/5)
    i=i+1

tr.penup()
tr.done()