from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdywQ7eIMRIHwd6qC4NMpbHjaZ4UYpw82xTSUbJ7LlYI2RPsQ/viewform?usp=sf_link")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
