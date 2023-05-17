from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    args = request.args
    name = args.get("name")
    message = args.get("message")
    return render_template("index.html", name=name, message=message)


if __name__ == '__main__':
    app.run()
