from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'





app.route("/porto")
def porto():
    return "<p>This is my porto</p>"
        #render_template("porto.html")



if __name__ == '__main__':
    app.run()
