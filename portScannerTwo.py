# Python3 program to check
# URL is valid or not
# using regular expression
import re
 
# Function to validate URL
# using regular expression
def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
 


##########################################################################################

def scanPort(userInput) :
    print("Initiating scan against url: ", userInput)

##########################################################################################
while(True) :
    url = input()
    
    if(isValidURL(url) == True):
        scanPort(url)
        break
    elif(url == "exit"):
        break
    else:
        print("Please input valid url: ")
        continue
# This code is contributed by avanitrachhadiya2155