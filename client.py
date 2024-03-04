from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

resultResponse = "False"
numberResponse = "False"

# Sends input to server
# If input is not a valid method, False is received
# Keeps asking until response is not False
while resultResponse.strip() == "False":
    sentence = input('Input either random, add or subtract: ')
    clientSocket.send(sentence.encode())
    resultResponse = clientSocket.recv(1024).decode()
    print('From server: ', resultResponse)

# Sends input to server
# If input is not 2 valid numbers, False is received
# Keeps asking until response is not False
while numberResponse.strip() == "False":
    numbers = input('Enter 2 numeric values, seperated by a space: ')
    clientSocket.send(numbers.encode())
    numberResponse = clientSocket.recv(1024).decode()
    print('From server: ', numberResponse)

clientSocket.close()