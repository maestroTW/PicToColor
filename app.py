import base64
from flask import Flask, render_template, request
from io import BytesIO
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['image_file']
    if image_file.filename == '':
        return 'Ошибка: выберите файл.', 400

    result = main.make_coloring_page(image_file.stream)

    buffer = BytesIO()
    result.save(buffer, format='JPEG')
    img = b'<img src="data:image/jpeg;base64,' + base64.b64encode(buffer.getvalue()) + b'"/>'

    return f''' <html> <head><title>Result</title></head> <body> {img.decode()} </body> </html> '''


if __name__ == '__main__':
    app.run()