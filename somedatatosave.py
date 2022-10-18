data = 'some data to save'

def read():
    with open('data.txt', 'r') as readFile:
        file.close()

def write():
    with open('data.txt' , 'w') as file:
        file.write(data + '\n')
        file.close()

def append():
    with open('data.txt' , 'a') as file:
        file.write(data + '\n')
        file.close()
append()
        
