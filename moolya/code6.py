#formating the string
# combining two strings
a="my name is sumedha"
b="how are you"
print("welcome",a,b)
print(a,b,"welcome")
print("welcome",b,a)
print("welcome {} {}".format(a,b))# using the formate
print("welcome {1} {0}".format(a,b)) # reversing the things
print("welcome {about} {question}".format(about=a,question=b)) #string formating