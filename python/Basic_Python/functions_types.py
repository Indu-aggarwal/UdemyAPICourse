class SecondClass:
        #function with no parameter and return value
        def hello(self):
                print("Hi python classes!")

        #function that takes 2 parameters, sum the values and print the value
        def sum(self, a, b):
                c = a + b
                print("The sum is:", c)

        # function that takes 2 parameters, multiply and return the value
        def multiply(self, a, b):
                return a * b

# class_object = SecondClass()
# class_object.hello()
# class_object.sum(2,3)
# print("Multiplication function is = ", class_object.multiply(2,2))
