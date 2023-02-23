#sets sets in unorderd homogeniues
# no duplicate are allowed
s={10,5,89,4,4,"A","F"}
print(s)
print(len(s))
print(30 in s)
print(20 in s)
s.add(500)
print(s)
s.pop()
s1={15,25,35,45,87}
s2={15,17,56,55,47,87}
z=s1.union(s2)
print(z)
y=s1.symmetric_difference(s2)
print(y)
s3={15,25}
print(s3.issubset(s1))
s3={10,25,55,78}
print(s3.issubset(s1))
s3.discard(10)
print(s3)
#s3.discard(55,78)
#print(s3)
