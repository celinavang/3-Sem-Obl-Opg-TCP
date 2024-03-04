from socket import *
import random
import json

def options(data):

    numResult = False

    # sets values
    method = data["method"].upper()
    num1 = data["num1"]
    num2 = data["num2"]

    # checks if both numbers are numbers
    numResult = isnumber(num1, num2)
    if numResult != True:
        # returns error
        return numResult

    # Method is "random"
    if method.strip() == "RANDOM":
        # checks if num1 is the smaller 
        if int(num1) <= int(num2):
            # returns result
            return "Your result is:  " + str(random.randint(int(num1), int(num2)))
        else:
            #returns result
            return "Your result is:  " + str(random.randint(int(num2), int(num1)))
    
    # Method is "add"
    elif method.strip() == "ADD":
        # returns result
        return "Your result is:  " + str(int(num1)+int(num2))
    
    # Method is "subtract"
    elif method.strip() == "SUBTRACT":
        # returns result
        return "Your result is:  " + str(int(num1)-int(num2))
    
    # Method is invalid
    else:
        # returns error
        return "Method: " + method + " does not exist" 

def isnumber(num1, num2):
    if num1.isnumeric() == False or num2.isnumeric() == False:
        # returns error
        return "Numbers " + num1 + " or " + num2 + " are not valid"
    else:
        return True
    
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()

    # waits for data
    data = connectionSocket.recv(1024).decode()

    # loads json data
    json_data = json.loads(data)

    result = options(json_data)

    # sends result or error message
    connectionSocket.send(result.encode())

    connectionSocket.close()
