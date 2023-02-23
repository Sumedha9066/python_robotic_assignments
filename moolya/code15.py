# return statement
def add(a,b,c):  # a,b,c are parameters
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a+b+c
z = add (5 , 5 , 5)  # 5,5,5 are arrguments
print(z)

# types of arguments
# position argument
# keyword argument
# required argument
# optional argument

def feb(num):
    a=0
    b=1
    i=0
    while i<num:
        print(a,end=" ,")
        c=a+b
        a=b
        b=c
        i+=1

n=int(input("enter the number:"))
fib=feb(n)
print(fib)
