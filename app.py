from flask import Flask, render_template, request, redirect, url_for
import os
from model.classify.predict import classify_image
from model.classify.room_cleaner import analyze_room

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected file", 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)

    # Use your existing classifier
    result = classify_image(image_path)
    return render_template('result.html', result=result, image_path=image_path)

@app.route('/room', methods=['POST'])
def room_analyze():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected file", 400

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)

    # Simulated detected items (we’ll automate later)
    detected_items = ["clothes", "books", "trash"]
    result = analyze_room(detected_items)
    return render_template('room.html', result=result, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
