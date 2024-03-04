from socket import *
import random

def options():
    # waits for method
    method = connectionSocket.recv(1024).decode()

    # method to upper to ignore case-sensitivity
    method = method.upper()
    numResult = False

    # Input is "random"
    if method.strip() == "RANDOM":
        # responds with selected method
        connectionSocket.send("You chose random".encode())
        while numResult == False:
            # checks if there are 2 numbers
            # checks if is a number
            numResult = number()
        # Sets order of numbers - smallest first
        if int(numResult[0]) <= int(numResult[1]):
            # returns result
            return random.randint(int(numResult[0]), int(numResult[1]))
        else:
            # returns result
            return random.randint(int(numResult[1]), int(numResult[0]))
    
    # Input is "add"
    elif method.strip() == "ADD":
        # responds with selected method
        connectionSocket.send("You chos add".encode())
        while numResult == False:
            # checks if there are 2 numbers
            # checks if is a number
            numResult = number()
        # returns result
        return int(numResult[0])+int(numResult[1])
    
    # Input is "subtract"
    elif method.strip() == "SUBTRACT":
        # responds with selected method
        connectionSocket.send("You chose subtract".encode())
        while numResult == False:
            # checks if there are 2 numbers
            # checks if is a number
            numResult = number()
        # returns result
        return int(numResult[0])-int(numResult[1])
    
    # Input is invalid
    else:
        # responds with False
        connectionSocket.send("False".encode())
        return False

def number():
    # waits for input
    number = connectionSocket.recv(1024).decode()

    # splits input
    number = number.split()
    
    # checks if there are two values entered
    if len(number) != 2:
        return False
    else:
        #checks if both are numbers
        for item in number:
            if item.isnumeric() == False:
                return False
        return number
    

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    
    
    valid_result = False
    # loops until we have a result
    while valid_result == False:
        valid_result = options()

    # sends result
    connectionSocket.send(("Your result is "+str(valid_result)).encode())
    
    connectionSocket.close()
