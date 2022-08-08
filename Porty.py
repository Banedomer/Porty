import sys
import socket
from datetime import datetime
  
print("Porty ver: 0.00001")

#getting the ip of a target
print("Please, write the IP of the Target:")
target = input()

#flashy cover 
print("-" * 70)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 70)
  
try:
     
    # will scan ports between 1 to 65,535 
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # scaning itself
        socket.setdefaulttimeout(1) #setting the time for closure
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

#error codes:
except KeyboardInterrupt:
        print("\n Alt+F4 !")
        sys.exit()
except socket.gaierror:
        print("\n Hostname could bot be reached !")
        sys.exit()
except socket.error:
        print("\n Server is dead !")
        sys.exit()
