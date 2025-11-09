import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load model only once to save time
model = load_model('model/saved/eco_model.h5')

class_labels = ['Recyclable', 'Non-Recyclable', 'Wet', 'Dry']

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    prediction = model.predict(x)
    result = class_labels[np.argmax(prediction)]
    return result
