import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hello, CS686!\nDocker is pretty great!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
