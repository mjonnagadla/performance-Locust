#Inhertance: Acquiring the properties of parent to child (or) base class to child class and use it 
#when ever is needed
#Advantages: Code readability and reusability is maintained across framework
#Types of Inheritance (Single, Multiple, Multilevel, Hierarchical)

#Single Inheritance
#when a class is derived from single parent class
class parent:
    def func1(self):
        print('Parent Class of Single Inheritance')

class child(parent):
    def func2(self):
        print("Child Class of Single Inheritance")

ob=child()
ob.func1()
ob.func2()

print("###########################")

#Mulitple Inheritanceclass 
#When a class can be dervied from more than one base class
class Mother(object):
    def __init__(self):
        self.str1 = "Mother"
        print("Mother Multiple")
    def show(self):
        print('mother')
 
class Father(object):
    def __init__(self):
        self.str2 = "Father"       
        print("Father Multiple")
 
    def show(self):
        print("father")

class Son(Father, Mother):
    def __init__(self):
        #Inside Derived class constructor we are initializing the base classes constructor(INIT) fucntion
        Mother.__init__(self)
        Father.__init__(self)
        print("Derived")
         
    def printStrs(self):
        print(self.str1, self.str2)
            
#Creating an object for derived class and access the variables of Parent base classes
ob = Son()
ob.printStrs()
ob.show()

print("###########################")

#Multi level Inheritance
#When a derived class from a parent class is parent to another child class
class grandparent:
    def func3(self):
        print('Grand Parent of Multilevel')

class parent(grandparent):
    def func4(self):
        print('Parent Class of Multilevel')

class child(parent):
    def funct(self):
        print("Child class of Multilevel")

ob1=child()
ob1.func3()
ob1.func4()
ob1.funct()

print("###########################")

# Hierarchical Inheritance
#One parent and multiple childs are derived is hierarchical
#Base class
class Parent:
      def func1(self):
          print("This function is in parent class of Hierarchical.")
 
# Derived class1
class Child1(Parent):
      def func2(self):
          print("This function is in child 1 of Hierarchical.")
 
# Derivied class2
class Child2(Parent):
      def func3(self):
          print("This function is in child 2 of Hierarchical.")
  
#creating objects of child classes and accessing the functions of Parent and thier's
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()