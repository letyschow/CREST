# import validators
import sys
import re
import socket

def scanPort(userInput) :
    print("Initiating scan against url: ", userInput)

url = input()

scanPort(url)

#create array to collect open ports
socket.setdefaulttimeout(1)

#create counter
count = 0
openPorts = []
for i in range(79,445) :
    #print a progress message on every 10th iteration
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    count+=1
    if count%10 == 0 :
        print("checking port ", i)
    # sock.settimeout(1)
    # print ("connecting on ", i)
    try:
        sock.connect((url, i))
        # print("connected to port ", i)
        openPorts.append(i)
        sock.close()
    except Exception as ex:
        pass
        # print(ex)
#print open ports array here
print(openPorts)