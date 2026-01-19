import socket

target = "127.0.0.1" #Scanning Local Host
ports = [21, 22, 80, 443, 3389] # Common ports to Chack

print(f"Scanning {target}...")

for port in ports:
    #Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) #Don't want to wait forever

    #Attempt to connect
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")

    s.close()

    """
    Key Concepts:
    - Libraries: import socket brings in networking tools.
    - For Loop: for port in port: repeats the check for every item in our list.
    - Error Handling: connect_ex returns an error code (0 means success) instead of crashing the script.
    """