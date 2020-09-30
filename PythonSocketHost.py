import socket

print("#####################")
print("# Python Port Maker #")
print("#                   #")
print("# Python 3.8 Socket #")
print("#     Connector     #")
print("#                   #")
print("#      By Riley     #")
print("#####################")

print(' [*] Be Sure To use https://github.com/Thman558/Just-A-Test/blob/master/socket%20client.py on the other machine')

host = input(" [*] What host would you like to use? ")
port = int(input(" [*] What port would you like to use? "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))

server_socket.listen(5)

print("\n[*] Listening on port " + str(port) + ", waiting for connections.")

client_socket, (client_ip, client_port) = server_socket.accept()
print("[*] Client " + client_ip + " connected.\n")

while True:
    try:
        command = input(client_ip + "> ")
        if len(command.split()) != 0:
            client_socket.send(bytes(command, 'utf-8'))
        else:
            continue
    except EOFError:
        print("ERROR INPUT NOT FOUND. Please type 'help' to get a list of commands.\n")
        continue

    if command == "quit":
        break

    data = client_socket.recv(1024).decode()
    print(data + "\n")

client_socket.close()