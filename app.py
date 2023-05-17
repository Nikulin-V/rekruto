from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    args = request.args
    name = args.get('name') if args.get('name') else 'имя'
    message = args.get('message') if args.get('message') else 'Текст сообщения'
    return render_template('index.html', name=name, message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
