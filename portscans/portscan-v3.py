from queue import Queue  # Threading allows to run scans simultaneously.
import socket            # Import the socket module to allow connections to other hosts and ports
import threading         # Queue helps multiple threads in a single instance like the port numbers  

try: 
    queue = Queue()
    open_ports = []
    target = input("Enter target: ")  # Entering a target to scan for open ports

    def portscan(port):               # Created a function to define the port scanner
        try:
            sock = socket.socket()    # Connecting to IPV4 with TCP 
            sock.connect((target, port)) # Targeting the target and ports 
            return True
        except:
            return False

    def open(mode): # Created 3 possible scanning modules
        if mode == 1:  
            for port in range(1, 1024): # Scanning for the well known ports 
                queue.put(port)
        elif mode == 2:
            for port in range(1, 49152): # Scanning for the reserved ports 
                queue.put(port)
        elif mode == 3: 
            ports = [20, 21, 22, 23, 25, 53, 80, 110, 443] # Scanning for the important ports
            for port in ports:
                queue.put(port)

    def execute(): # The execute function gets the port number from the queue and print the results
        while not queue.empty(): # As long as the queue is not empty, it wil continue to scan on the next port
            port = queue.get()   # Whatever port is open, it will add to the list
            if portscan(port):
                print("Port %d is open!"% (port)) # Printing all open ports 
                open_ports.append(port) # Appending the open ports to the list

    def scanner(threads, mode):

        open(mode)

        thread_list = []

        for x in range(threads):  # Loading the ports and creating a new empty list for our threads.
            thread = threading.Thread(target=execute) # Creating the desired amount of threads, assign to the scanner function while adding them to the list. 
            thread_list.append(thread)

        for thread in thread_list: # Starting the threads, now scanning all the ports with the for loop.
            thread.start()

        for thread in thread_list:
            thread.join()

        print("Open ports are:", open_ports) # Threads finished and now printing out all the open ports.

    scanner(50, 1) # Running the function like this allows us to scan the ports. You can change the threads on the first parameter scans the port, the second paramter is per second (EX: 50 ports per second)

except:
    print('Enter a valid host!')