#print("*")
#print("*","*")
#print("*","*","*")

#dictionary:is used for
a={"url1":"google.com","url2":"amazon.com"}
b={1:"sumedha",2:"moolya"}
print(b[1])
print(a["url1"])
b[3]="flipkart.com"
print(b)
print(b.get(1))#get method
print(b.keys())
print(b.items())#values comes with value
print(b.values()) #only values will appear
print(b.pop(1))
print(b.keys())
print(b.popitem()) # to remove the last value only.
print(b.keys())
b.update({3:"demo.com",4:"guru99"})# update the keys
print(b)
b.setdefault(5,"youtube.com")# updating the keys by usimg the set default
print(b)
b.clear()# empty dictionary
print(b)
