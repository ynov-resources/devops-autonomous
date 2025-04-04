from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    response = "Hello, {ip}, your User-Agent is: {ua}".format(ip=ip, ua=ua)
    return "<p>"+response+"</p>"


app.run(host='0.0.0.0', port=8080)
