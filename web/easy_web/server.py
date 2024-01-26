from flask import Flask, render_template, make_response
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

app = Flask(__name__)
@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    for i in range(0, 25):
        s = generate_random_string(44)
        response.set_cookie(f"cookie{i+1}", s)
    response.set_cookie(f"cookie26", "Q09QU3tjMDBrMTM1X2M0bl9jNHU1M19kMXNhczczcnN9")
    for i in range(26, 40):
        s = generate_random_string(44)
        response.set_cookie(f"cookie{i+1}", s)
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=41340)
