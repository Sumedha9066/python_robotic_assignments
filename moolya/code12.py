# list1=["moolya","python","learning"]
# for x in list1:
#      for y in x:
#        print(y)
#
# list2="sumedha"
# for y in list2:
#     print(y)

# list3=[["a","b","c"],["d","e","f"]]
# for z in list3:
#     for a in z:
#         print(a)


list4=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
#my country name is +country+ and i live in +city
for b,c in list4:
    print("my country is " +b+ " and i live in "  +c)

dict1=dict(list4)
for i,j in dict1.items():
    print(i,j)

print(dict1)
list5=["my","name","is","sumedha"]
set1 = set(list5)
print(set1)
tuple1=tuple(list4)
print(tuple1)


