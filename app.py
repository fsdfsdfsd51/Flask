from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSe1mj2eeao33uiij-ZGE2dwpPsp6SYywZN5Rs44L8a58PR8fg/viewform?usp=sf_link")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
