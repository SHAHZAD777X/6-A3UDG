class fun:
    def __init__(self):
       self.str1=""
    
    def getString(self):
       self.str1=input("Enter a string:")

    def printString(self):
       print("Result:",self.str1.upper())

s1=fun()
s1.getString()
s1.printString()