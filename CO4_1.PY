class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth


    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

r1=rectangle(10,20)
r2=rectangle(20,30)
print("area of first rectangle=",r1.area())
print("area of second rectangle=",r2.area())
print("perimeter of first rectangle:",r1.perimeter())
print("perimeter of second rectangle:",r2.perimeter())



    
