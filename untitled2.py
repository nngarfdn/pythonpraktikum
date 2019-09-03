#Program mencari jarak titik

import math

x1 = int(input("Masukan nilai x1 = "))
x2 = int(input("Masukan niali x2 = "))
y1 = int(input("Masukan niali y1 = "))
y2 = int(input("Masukan niali y2 = "))

d = int(math.pow(math.pow(x2-x1, 2) + math.pow(y2-y1, 2),0.5))
print ("jaraknya adalah ", d)