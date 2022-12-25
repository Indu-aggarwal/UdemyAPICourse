from distutils import text_file
import re

def read_whole_data():
        open_file = open("text_file.txt", 'r')
        return open_file.read() # read all the data in a text file
read_data = read_whole_data()

def read_single_line():
        open_file = open("text_file.txt", 'r')
        return open_file.readline()

def read_num_characters():
        open_file = open("text_file.txt", 'r')
        return open_file.read(5)

def read_all_characters(txt_data):
        result = []
        for num in txt_data:
                result.append(num)
        return result

def read_all_lines(txt_data):
        while (txt_data):
                return txt_data



print("Text file content is:\n", read_data)
print("Text file single line is:\n", read_single_line())
print("The characters are:\n", read_num_characters())
print("All characters are: ", read_all_characters(read_data))
print("Print each line: \n", read_all_lines(read_data))

