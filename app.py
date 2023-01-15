from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Deployed using GitOps version1.4/New Code for CLI /1234567890'
