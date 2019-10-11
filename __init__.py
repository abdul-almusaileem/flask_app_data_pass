
# this app is to be backend for a simple html to parse data from a form
#
from flask import Flask, request, render_template

# create the app 
#
app = Flask("__name__")


@app.route("/")
def hello_world():
    return "hello world!"

@app.route('/angles', methods = ['GET'])
def get_angles():
    return render_template("form.html")



#
#
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
    