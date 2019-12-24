import select
import socket
import time

inputs = list()
outputs = list()
clients = list()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 9090))
server.listen(5)

inputs.append(server)
print("Server is running, please, press ctrl+c to stop")

try:
    while inputs:
        readables, writables, exceptional = select.select(inputs, outputs, inputs)

        for resource in readables:

            if resource is server:
                connection, client_address = resource.accept()
                connection.setblocking(0)
                inputs.append(connection)
                if client_address not in clients:
                    clients.append(client_address)

                time_ = time.strftime('%Y - %m - %d - %H.%M.%S', time.localtime())
                print(client_address, time_)
            else:

                data = ""
                try:
                    data = resource.recv(1024)
                    print(data.decode('utf-8'))

                except ConnectionResetError:
                    pass

                if data:

                    if resource not in outputs:
                        outputs.append(resource)
                    for client in clients:
                        if client != client_address:
                            resource.sendto(data, client)

                else:

                        if resource in outputs:
                            outputs.remove(resource)
                        if resource in inputs:
                            inputs.remove(resource)
                        resource.close()

except KeyboardInterrupt:
    clear_resource(server_socket)
    print("Server stopped!")
