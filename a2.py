class Employee:
    def __init(self):
        print('Employee class initialized')

    def __del__(self):
        print("Calling Destructor")

def objfun():
    print('Object created')
    obj = Employee()
    print('object function end')
    return obj

print('Calling function')
obj = objfun()
print('Program end')