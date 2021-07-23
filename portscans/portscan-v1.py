import socket # Import the socket module to allow connections to other hosts and ports

try:
    sock = socket.socket() # Created a sock connection, if left blank will use TCP and IPV4 by default
    target = input ('Enter Target: ') # Target host
    port = int(input('Enter Port: ')) # Enter a port number 
    ip = socket.gethostbyname(target) # Obtain the IP of the target 

    def Scan(): # Define a function for the scan
        if sock.connect_ex((target,port)): # If the target and port exists 
            print ('Port {} is closed!'.format(port))
        else:
            print ('Port {} is opened!!'.format(port))
    Scan()
except:
    print ('Enter valid target and port!')

