from socket import *
import json

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Asks for all 3 inputs at once
data = {
        "method": input('Enter method: '),
        "num1": input('Enter first number: '),
        "num2": input('Enter second number: ')
        }

# Creates json object 
json_object = json.dumps(data)
# Sends json object
clientSocket.send(json_object.encode())
# Receives response
# Response is either result or error message
response = clientSocket.recv(1024).decode()

print(response)

clientSocket.close()