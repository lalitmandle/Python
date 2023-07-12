# class tamdem:
#     id = 230
#     name = "sam"
#     def display (self):
#         print("ID : %d \nName: %s"%(self.id,self.name))
# c = tamdem()
# c.display()

class Parent: #defind parent class
    def myMethod(self):
        print("Calling parent method")
class Child(Parent): #define child class
    def myMethod(self):
        print("calling child method ")
c = Child() # instance of child
c.myMethod  # child calls overridden method