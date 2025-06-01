from flask import Flask, render_template

try:
    from werkzeug.urls import url_quote as quote  # Werkzeug <2.0
except ImportError:
    try:
        from werkzeug.utils import quote  # Werkzeug 2.0.x
    except ImportError:
        from urllib.parse import quote  # Fallback to stdlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Ansible-Deployed App!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
