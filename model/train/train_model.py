import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

def train_model():
    train_dir = 'dataset/train'
    test_dir = 'dataset/test'
    
    # Data preprocessing
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_set = train_datagen.flow_from_directory(train_dir, target_size=(128,128), batch_size=16, class_mode='categorical')
    test_set = test_datagen.flow_from_directory(test_dir, target_size=(128,128), batch_size=16, class_mode='categorical')

    # CNN model
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(4, activation='softmax')
    ])

    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    # Train
    model.fit(train_set, epochs=10, validation_data=test_set)

    # Save model
    os.makedirs('model/saved', exist_ok=True)
    model.save('model/saved/eco_model.h5')
    print("✅ Model training completed and saved successfully at model/saved/eco_model.h5")

if __name__ == '__main__':
    train_model()
