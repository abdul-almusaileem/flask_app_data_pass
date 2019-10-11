
import socket


# the ip and the port of the server
#
HOST = '0.0.0.0'
PORT = 65432

def main():
    # create the socket obj
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        # connect to the server
        #
        sock.connect((HOST, PORT))

        # receive from the server
        #
        data = sock.recv(1024)
        print ("Received", repr(data))


if __name__ == '__main__':
    main()
