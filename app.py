#!/usr/local/bin/python3

import os
from flask import Flask

app = Flask(__name__)
podname = os.uname()[1]

@app.route("/")
def index():
    return render_template('test.html')
    #return " Container hsw | POD Working : " + podname + " | v=1\n"

if __name__ == "__main__":
    app.run()
    #app.run(host="0.0.0.0", port="5000")
