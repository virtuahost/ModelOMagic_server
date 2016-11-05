import sys

sys.path.append("lib/Leap")
sys.path.append("lib/x86")
sys.path.append("lib/")

import Leap, socket, ctypes

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)
controller = Leap.Controller()

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        while True:
            frame = controller.frame()
            data = frame.serialize
            serialized_data = data[0]
            serialized_length = data[1]
            data_address = serialized_data.cast().__long__()
            buffer = (ctypes.c_ubyte * serialized_length).from_address(data_address)
            if data:
                connection.sendall(buffer)
            else:
                break
            
    finally:
        connection.close()