def read_data():
        data_file = open("writen.txt",'r')
        return data_file
file_data = read_data()

def data_handling(data):
        return data.readline()

print(file_data.tell())
print(data_handling(file_data).tell())
