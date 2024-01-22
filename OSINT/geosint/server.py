from flask import Flask, request, render_template, render_template_string, redirect
import subprocess
import urllib
import json

challs = json.load('challs.json')

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/chall/chall_id')
def view_chall(chall_id):
    try:
        chall_url = challs["chall_id"][chall_id]["url"]
        return render_template('chall.html', chall_id=chall_id, pan_url=chall_url)
    except:
        return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=51337)
