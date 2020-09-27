import socket

print("#####################")
print("# Python Port Maker #")
print("#                   #")
print("#'To Go Boldy Where'#")
print("#  No Other Python  #")
print("#      Has Gone     #")
print("#      By Riley     #")
print("#####################")

 
HOST = "192.168.0.17"  # server will bind to any IP
PORT = 12345
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates server TCP socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # prevents from getting timeout issues
server_socket.bind((HOST, PORT))
 
server_socket.listen(5)  # 5 connections max in queue
print("\n[*] Listening on port " +str(PORT)+ ", waiting for connections.")
 
# see socket documentation to understand how socket.accept works
client_socket, (client_ip, client_port) = server_socket.accept()
print("[*] Client " +client_ip+ " connected.\n")
 
 
while True:
    try:
        command = "raw_input" (client_ip+ ">")
        if(len(command.split()) != 0):
            client_socket.send(command)
        else:
            continue
    except(EOFError):
            print("Invalid input, type 'help' to get a list of implemented commands.\n")
            continue
 
    if(command == "quit"):
        break
 
    data = client_socket.recv(1024)
    print(data + "\n")
 
client_socket.close()