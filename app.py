from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

import porto
app.register_blueprint(porto.bp)




