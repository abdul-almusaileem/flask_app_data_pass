
import socket
import struct


HOST = "172.31.34.239"  #"54.152.44.140"
PORT = 5001

def main():
    # create the socket
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        # bind the socket to the specified port
        #
        sock.bind((HOST, PORT))

        # listen for connections
        #
        sock.listen()

        while True:

            # get the connection 
            #
            conn, addr = sock.accept()

            with conn:
                print("Connected by {}".format(addr))

                while True:
                    # receive data
                    #
                    data = conn.recv(4)
                    if (data == b''):
                        break
                    #print("got:  {}".format(data))
                    data_f = struct.unpack("f", data)[0]
                    print("got:  {}".format(data_f))

                    # break after recieving all the data
                    #
                    if not data:
                        break

if __name__== '__main__':
    main()
