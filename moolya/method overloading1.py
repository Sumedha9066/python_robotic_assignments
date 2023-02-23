from multipledispatch import dispatch
import math
@dispatch(int)
def sum(a):
    print(a*a)

@dispatch(int,int)
def sum(a,b):
     print(a+b)
    
@dispatch(int,int)
def sum(a,b):
    print(a*b)

@dispatch(int,int)
def sum(a,b):
    sq=a*b

    i=int(math.sqrt(sq))
    if i**2==sq:
        print("this is a perfect square: ",sq)
    else:
        print("this is not a perfect square: ",sq)

sum(1,9)
sum(2)
sum(5,5)
sum(5,5)
