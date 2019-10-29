n = int(input())

def bintang(n) :
  for i in range (n) :
    for j in range (n) :
      print("*", end="")
    print()

def segitiga(n) :
  for i in range(n):
     for j in range(i+1):
        print('*', end='')
     print()
     


bintang(n)
print()
print()
print()
segitiga(n)
