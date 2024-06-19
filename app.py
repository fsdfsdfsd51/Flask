from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_redirect():
    return redirect(random.choice(["https://docs.google.com/forms/d/e/1FAIpQLSe$

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
