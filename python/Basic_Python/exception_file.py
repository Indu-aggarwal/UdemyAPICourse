user_input1 = input("Please enter first number: ")
user_input2 = input("Please enter second number: ")

def input_sum(num1, num2):
        try:
                return int(num1) + int(num2)
        except:
                return "You enter invalid value"


print(input_sum(user_input1,user_input2))

