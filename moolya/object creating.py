# collection of objects is called class
class my_class:
    y,z=5,5
    def add(self,a,b):
        self.y=a
        self.z=b
        print(self.y+self.z)


obj=my_class()   #creation of class
obj.add(20,20)  # self is a keyword 
obj.add(10,10)

