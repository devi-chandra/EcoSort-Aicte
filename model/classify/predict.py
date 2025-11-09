import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from model.classify.eco_guide import eco_suggestions

# Load trained model
model_path = "model/saved/ecosort_model.h5"
model = tf.keras.models.load_model(model_path)

# Class names (same as dataset folders)
class_names = ["recyclable", "non-recyclable", "wet", "dry"]

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    print(f"♻️ Predicted: {predicted_class} ({confidence:.2f}% confidence)")
    print("💡 Suggestion:", eco_suggestions(predicted_class))

# Example usage:
# classify_image("dataset/test/recyclable/sample.jpg")
