from flask import Flask, render_template
from werkzeug.utils import quote

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Ansible-Deployed App!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
