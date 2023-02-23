# def math(b):
# if a=5+b**2+4
#     print("the entered number is a perfect square")
#  else if a=5+b**2-4:
#          print("its a perfect square")
# else
#   print("not a perfect square")
#   math(25)
y=int(input("enter the number of terms: "))
a=0
b=1
c=0
for i in range(y):
    print(c,end=" ")
    a=b
    b=c
    c=a+b