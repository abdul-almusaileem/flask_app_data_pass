
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

        return "{}".format(angles)

    else:
        return render_template('from.html')    
    
    # #
    # #
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     pass

    #     # bind the socket to a specific address and a port
    #     #
    #     sock.bind(('0.0.0.0', 65432))
        
    #     sock.listen()
        
    #     while True:
            
    #         # wait for connections from clients
    #         #
    #         conn, add = sock.accept()  
            
    #         with conn:
    #             print ("Connected by", add)
    #             conn.sendall(angles)
        


#
#
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
    