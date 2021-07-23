import socket # Import the socket module to allow connections to other hosts and ports 

target = input ('Enter Target IP: ')

def portscan(port): # Created a function to define the port scanner
 try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Created a sock connection on IPV4 using TCP
    sock.connect((target, port)) # Using my localhost as a target 
    return True # Returns true if the statement is valid 
 except:
    return False # Returns false if the statement is false 

for port in range(1, 1024): # Making a for loop to scan the well known ports (port 1-1024)
 result = portscan(port) # Creating a variable for the results 
 if(result): 
    print("Port {} is open!".format(port)) # Printing out the open ports
 else:
    print("Port {} is closed!".format(port)) # Printing out the closed ports