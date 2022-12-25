from math import ceil


data = "  Hello this is Testing World  "

def string_len(str):
        return len(str)

#remove space from left
def rm_space_left(str):
        return len(str.lstrip())

#remove space from right
def rm_space_right(str):
        return len(str.rstrip())

# replace function
def replace_string_content(str):
        new_str = str.casefold() # case insensitive matching
        return new_str.replace("t", "###")

# space remove
def rm_space(str):
        return len(str.replace(" ", ""))

# find data in the string
def find_data(str):
        return str.find("The")

# spit a string
def sting_split(str):
        return str.split()

print("The length of the string is:",string_len(data))
print("The string after left space removed is:",rm_space_left(data))
print("The string after right space removed is:",rm_space_right(data))
print("String after replacing:",replace_string_content(data))
print("String with no space is length:", rm_space(data))
print(find_data(data))
print(sting_split(data))
