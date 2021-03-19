from flask import Flask
from flask import url_for, request, render_template

app = Flask(__name__)


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        print(request.files['file'])
        with open(request.files['file'], 'r') as file:
            return file.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
