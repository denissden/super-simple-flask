import os

from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.route('/')
def image():
    return render_template("main.html")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
