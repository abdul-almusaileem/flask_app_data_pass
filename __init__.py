
# this app is to be backend for a simple html to parse data from a form
#
from flask import Flask, request, render_template
import socket
# create the app 
#
app = Flask("__name__")


@app.route("/")
def index():
    return render_template('from.html')

@app.route('/', methods = ['GET', 'POST'])
def get_angles():
    if request.method == 'POST':
        angles = []
        angles.append(request.form["base"])
        angles.append(request.form["elbow high"])
        angles.append(request.form["elbow low"])
        angles.append(request.form["middle"])
        angles.append(request.form["wrist"])
        angles = [float(angle) for angle in angles] 

        send_angles(angles=angles)
        return "{}".format(angles)

    else:
        return render_template('from.html')    
   
   # this method is to test sockets to send data
   #
def send_angles(angles=[]):
    # declare constants
    #
    HOST = "54.152.44.140"
    PORT = 5001
    
    # initiate the socket 
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        # open the socket connection for the specifide host and port
        #
        sock.bind((HOST, PORT))
        
        # let the socket listen for connections
        #
        sock.listen()
        
        # keep runing
        #
        while True:
            
            # accept connection from clients
            #
            conn, add = sock.accept()
    
            with conn:
                print("/"{}/", is connected".format(add))
                
                # while the connection is set
                #
                while True:
                    # send angles
                    # 
                    for angle in angles:
                        conn.sendall(angle)
                    


#
#
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
    
