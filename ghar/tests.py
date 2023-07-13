from django.test import TestCase


# Create your tests here.

# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "c"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__c)


# Driver code
obj1 = Derived()
print(obj1._Base__c)
