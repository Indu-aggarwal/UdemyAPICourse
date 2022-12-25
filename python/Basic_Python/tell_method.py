def tell_function():
        text_file = open("writen.txt", 'r')
        print(text_file.tell())
        text_file.readline()
        print(text_file.tell())

tell_function()
