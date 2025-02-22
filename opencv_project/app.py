from flask import Flask, render_template, request
from opencv_utils import process_image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    result = process_image(file)  # call OpenCv Fn
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
