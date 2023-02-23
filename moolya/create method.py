# def add(a,b):
#     global x # can use it anywhere means outside the method
#     x=20 # local variable
#     print(x)
#     print(a+b)


# def sub(a,b):
#     print(a-b)
#     print(x)

# def multiply(a,b):
#     x=20
#     print(x)
#     def sub(a,b):
#         print(x)
#     sub(10,5)
# multiply(10,5)

x=10
def multiply():

    print(x)
    def sub():
        x=30
        print(x)
        def add():
                     # when the local and glodal variable both are present both means prefrence will be "local variable"
            print(x)
        add()
    sub()
multiply()
