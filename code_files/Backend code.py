from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return open('/var/www/html/index.html').read()

@app.route('/forward')
def forward():
    print("Forward")
    return "OK"

@app.route('/backward')
def backward():
    print("Backward")
    return "OK"

@app.route('/left')
def left():
    print("Left")
    return "OK"

@app.route('/right')
def right():
    print("Right")
    return "OK"

@app.route('/stop')
def stop():
    print("Stop")
    return "OK"

app.run(host='0.0.0.0', port=5000)