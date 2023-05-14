import socket
host = socket.gethostname()
port = 5892
sock = socket.socket()
sock.bind((host, port))

sock.listen(2)
connection, address = sock.accept()

print("Connection from: " + str(address))

get_values = {}
get_op = ''

while True:
    final_output = connection.recv(1349).decode()
    final_output = final_output.split(" ")

    if final_output[0] == "GET":
        get_inp = get_values.get(final_output[1])
        if get_inp != 0:
            get_op = get_inp
            print("Get:", get_op)

    elif final_output[0] == "PUT":
        get_values[final_output[1]] = final_output[3]
        get_op = 'receieved final_output'
        print("Put:", get_op)

    elif final_output[0] == "DUMP":
        pair = get_values.keys()
        if pair != 0:
            get_op = " ".join(pair)
            print("Dump:", get_op)

        print(get_op)

    connection.send(get_op.encode())

sock.close()