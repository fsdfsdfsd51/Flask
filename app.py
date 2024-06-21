from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def random_redirect():
    return redirect(random.choice(["https://docs.google.com/forms/d/e/1FAIpQLSerCMQbpODwjCZn-47LczWw2nZyNmuhfgFn26T6WjQ1VJf4yg/viewform?usp=sf_link", "https://docs.google.com/forms/d/e/1FAIpQLSfZcyp5Gva0GvZmluhlSN2T8waO5opstlBC3D2i3uFnvMmJMw/viewform?usp=sf_link"]))
#    return redirect(random.choice(["https://docs.google.com/forms/d/e/1FAIpQLSerCMQbpODwjCZn-47LczWw2nZyNmuhfgFn26T6WjQ1VJf4yg/viewform?usp=sf_link", "https://docs.google.com/forms/d/e/1FAIpQLSfZcyp5Gva0GvZmluhlSN2T8waO5opstlBC3D2i3uFnvMmJMw/viewform?usp=sf_link", "https://docs.google.com/forms/d/e/1FAIpQLSdywQ7eIMRIHwd6qC4NMpbHjaZ4UYpw82xTSUbJ7LlYI2RPsQ/viewform?usp=sf_link", "https://docs.google.com/forms/d/e/1FAIpQLSe1mj2eeao33uiij-ZGE2dwpPsp6SYywZN5Rs44L8a58PR8fg/viewform?usp=sf_link"]))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
