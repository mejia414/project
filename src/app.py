from flask import Flask
from flask import jsonify

app = Flask(__name__,)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'response': 'hello world'})


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
