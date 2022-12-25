def print_using_format(str1, int):
        #one way of using format in print statement
        print(f"This is our sting {str1}\nThis is the integer {int}")
        #another way of using format in print statement
        print(f"This is our sting {str1}\nA decimal number: {int}, rounded to 2 decimal places: {int:.2f}")

print_using_format("Hello", 5.87934)
