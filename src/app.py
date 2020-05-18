from flask import Flask
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import Request
from flask import Response

app = Flask(__name__,)


@app.route('/', methods=['GET'])
def index():
    x = 'hello world'
    return render_template('index.html', x=x)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'response': 'hello world'})


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
