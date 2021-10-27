import socket
import re

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #To create the client socket
clientsocket.connect(('localhost', 8089)) #To join the server
print('Enter word : ')
inpt = input()
regex = re.compile('[ @_!#$%^&*()<>?/\|}{~:]')

#Checking the input
if len(inpt) <= 14 and regex.search(inpt) is None:
    print('Enter hint : ')
    hint = input()
    inpt = inpt + ',' + hint
    clientsocket.send(bytes(inpt, 'UTF-8')) #Sending the data to the server
    print("The message has been sent")
else:
    print('Please add the word of less than 10 characters and with no special characters')