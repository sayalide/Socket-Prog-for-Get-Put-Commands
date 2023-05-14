import socket
if __name__ == '__main__':
    host = socket.gethostname()
    port = 5892
    sock = socket.socket()
    sock.connect((host, 5892))
    proxy_server = {}

    gettype = input("Select either of one: PUT GET DUMP \n")
    temp_data = ''
    while True:
        splittype = gettype.split(" ")
        if splittype[0] == 'GET':
            if not splittype[1] in proxy_server:
                sock.send(gettype.encode())
                print('server started listening \n')
                final_output = sock.recv(1349).decode()
                proxy_server[splittype[1]] = final_output
            else:
                final_output = proxy_server[splittype[1]]
                temp_data = 'Output from Proxy Server: ' + str(final_output)

        else:
            sock.send(gettype.encode())
            print('server started listening \n')
            final_output = sock.recv(1349).decode()
        if final_output != 0:
            if temp_data:
                print(temp_data)
            else:
                print('final_output: ' + str(final_output))
        gettype = input("Select either of one: PUT GET DUMP \n")

    sock.close()
