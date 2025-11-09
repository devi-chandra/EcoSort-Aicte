from flask import Flask, render_template, request
from model.classify.predict import predict_image
from model.classify.eco_guide import get_eco_guide
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload_and_predict():
    file = request.files['image']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        label = predict_image(filepath)
        suggestion = get_eco_guide(label)
        return render_template('result.html', label=label, suggestion=suggestion, image_path=filepath)
    return render_template('index.html', error="Please upload an image.")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
