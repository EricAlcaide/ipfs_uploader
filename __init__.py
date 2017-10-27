# -*- coding: iso-8859-15 -
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import ipfsapi
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
vault = 'utils/vault.txt'
api = ipfsapi.connect('127.0.0.1', 5001)

def uploadFile(post_file):
    res = api.add(post_file)
    post_hash = res['Hash']
    return post_hash

def saveRecord(link, filename):
	datetime = str(time.time())
	with open(vault, 'w+') as f:
		f.write(datetime, filename, link)
	return


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/sent/',  methods = ['GET', 'POST'])
def search():
    file = request.files['file'] 
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload, filename))

        prev = 'https://ipfs.io/ipfs/'
        link = prev + uploadFile(upload+filename)
        saveRecord(link, filename)

        return render_template('sent.html', link=link)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

