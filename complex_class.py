class Complex:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    
    def display(self):
        if self.b>0:
            print("complex number is ",self.a,"+",self.b,"j")
        else:
            print("complex number is ",self.a,self.b,"j")
    
    def __add__(self,other):
        return Complex(self.a + other.a,self.b + other.b)
    def __sub__(self,other):
        return Complex(self.a - other.a,self.b - other.b)
    def __mul__(self,other):
        return Complex(self.a * other.a,self.b * other.b)
    
obj1= Complex(2,3)
obj2 =Complex(8,4)
obj3 = obj1+obj2
obj4 = obj1-obj2
obj5 = obj1*obj2
print("Sum")
obj3.display()
print("Difference")
obj4.display()
print("Product")
obj5.display()
