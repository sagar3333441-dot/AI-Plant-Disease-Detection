import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
import json

# Dataset path
DATASET_PATH = os.path.join(
    os.path.dirname(__file__),
    "dataset",
    "color"
)

# Settings
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
SEED = 123

# Dataset load karo
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
num_classes = len(class_names)

print("\nClasses:", num_classes)
print("Class names:")
for name in class_names:
    print(name)

# Performance improve
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# MobileNetV2 model
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False

# AI model
model = keras.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Rescaling(1.0 / 127.5, offset=-1),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Training
print("\nStarting training...\n")

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)

# Save trained model
model.save(
    os.path.join(os.path.dirname(__file__), "plant_disease_model.keras")
)

# Save class names
with open(
    os.path.join(os.path.dirname(__file__), "class_names.json"),
    "w"
) as f:
    json.dump(class_names, f, indent=4)

print("\n✅ Training completed!")
print("✅ Model saved as plant_disease_model.keras")
print("✅ Class names saved as class_names.json")