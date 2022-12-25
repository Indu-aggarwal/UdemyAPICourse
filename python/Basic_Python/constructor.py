# constructors always start with __init()__
# constructors are automatically called when object is created
# constructors never return value
class Constructor:
        def __init__(self, a, b):
                print("This is a constructor")

        def hello(self):
                print("Hi python classes!")

        def sum(self, a, b):
                return a + b

        def multiply(self, a, b):
                return a * b

num1, num2 = 1, 2
class_object = Constructor()
class_object.hello()
print("The sum function return: ", class_object.sum(num1, num2))
print("Multiplication function return = ", class_object.multiply(num1, num2))
