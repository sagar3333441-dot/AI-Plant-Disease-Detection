import os
import json
import numpy as np
import tensorflow as tf
from PIL import Image


# Model aur class names ka path
BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "plant_disease_model.keras"
)

CLASS_NAMES_PATH = os.path.join(
    BASE_DIR,
    "class_names.json"
)


# Trained AI model load karo
model = tf.keras.models.load_model(MODEL_PATH)


# Disease/class names load karo
with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)


def predict_disease(image_file):

    # Uploaded image ko open karo
    image = Image.open(image_file).convert("RGB")

    # Image ko model ke required size me convert karo
    image = image.resize((224, 224))

    # NumPy array me convert karo
    image_array = np.array(image, dtype=np.float32)

    # Batch dimension add karo
    image_array = np.expand_dims(image_array, axis=0)

    # AI prediction
    predictions = model.predict(image_array, verbose=0)

    # Highest probability class
    predicted_index = np.argmax(predictions[0])

    confidence = float(predictions[0][predicted_index]) * 100

    disease = class_names[predicted_index]


    return {
        "disease": disease,
        "confidence": f"{confidence:.2f}%",
        "cause": "Disease identified from the uploaded plant leaf image.",
        "remedy": "Remove affected leaves and follow suitable treatment for the identified disease.",
        "precaution": "Keep plants healthy, avoid excessive moisture, and monitor leaves regularly."
    }