import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model('model/ecosort_model.h5')

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(150,150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    classes = ['recyclable', 'non-recyclable', 'wet', 'dry']
    return classes[np.argmax(prediction)]


from eco_guide import get_eco_advice

if __name__ == "__main__":
    path = input("Enter the path of the image: ")
    category, confidence = classify_image(path)
    print("\n✨ Eco Advice ✨")
    advice = get_eco_advice(category)
    print("♻️ Reuse Ideas:")
    for idea in advice["reuse"]:
        print("-", idea)
    print("\n🚮 Safe Disposal:")
    for tip in advice["dispose"]:
        print("-", tip)
