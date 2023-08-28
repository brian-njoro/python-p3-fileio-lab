def write_file(file_name, file_content):
    with open(file_name + ".txt", mode = "w") as file1:
        file1.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + '.txt', mode = 'a') as file2:
        file2.write(append_content)

def read_file(file_name):
    with open(file_name + '.txt', mode = 'r') as file3:
        print(file3.read())
