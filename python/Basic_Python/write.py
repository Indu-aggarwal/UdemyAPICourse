def write_to_file():
        #file = open("writen.txt", 'w') # overwrite exsisting data
        text_file = open("writen.txt", 'a') #append to existing data
        text_file.write ("Writing to a file.\n")
        text_file.write ("This is a new line.\n")
        text_file.close

write_to_file()
