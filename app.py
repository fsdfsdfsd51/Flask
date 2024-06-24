from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSerCMQbpODwjCZn-47LczWw2nZyNmuhfgFn26T6WjQ1VJf4yg/viewform?usp=sf_link")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
