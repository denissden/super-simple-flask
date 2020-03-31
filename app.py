import os

from flask import Flask, url_for
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
@app.route('/image')
def image():
    return '''<img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/stay away.jpg'))


if __name__ == '__main__':
    app.run()
