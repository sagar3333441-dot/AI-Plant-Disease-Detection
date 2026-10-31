# 🌱 AI-Based Plant Disease Detection System

## 📌 Project Overview

The **AI-Based Plant Disease Detection System** is a machine learning-based web application designed to identify plant diseases from leaf images.

The system allows users to upload an image of a plant leaf and uses a trained deep learning model to predict whether the plant is healthy or affected by a disease.

This project aims to help farmers, students, and agricultural users identify plant diseases quickly and support better crop management.

## 🚀 Features

- 🌿 AI-based plant disease detection.
- 📷 Upload plant leaf images for disease prediction.
- 🤖 Trained machine learning/deep learning model.
- 🖥️ User-friendly web interface.
- 🔐 User Login and Signup.
- 📊 Dashboard for users.
- 📜 Prediction history.
- ⚡ Real-time prediction using the trained model.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend web framework |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend functionality |
| TensorFlow/Keras | Deep Learning Model |
| Machine Learning | Plant disease classification |

## 📁 Project Structure

```text
mini-project/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── dashboard.html
│   ├── history.html
│   ├── index.html
│   ├── login.html
│   └── signup.html
│
├── model/
│   ├── dataset/
│   ├── class_names.json
│   ├── model.py
│   ├── plant_disease_model
│   └── train_model.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Based-Plant-Disease-Detection.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Based-Plant-Disease-Detection
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python backend/app.py
```

### 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

The application will now run on your local machine.

## 🔍 How It Works

1. User opens the web application.
2. User logs in or creates an account.
3. User uploads an image of a plant leaf.
4. The uploaded image is processed by the AI model.
5. The trained model predicts the plant disease.
6. The prediction result is displayed on the dashboard.
7. Users can view their previous prediction history.

## 🤖 Model Information

The system uses a trained deep learning model for plant disease classification.

- Input: Plant leaf image.
- Processing: Image preprocessing and model prediction.
- Output: Predicted plant disease class.

## 🎯 Project Objectives

- Detect plant diseases using artificial intelligence.
- Reduce manual plant disease identification efforts.
- Provide a simple and accessible disease detection platform.
- Support early identification of plant diseases.

## 🔮 Future Scope

- Add more plant disease categories.
- Improve model accuracy using larger datasets.
- Support multiple crop types.
- Add multilingual support.
- Deploy the application on a cloud platform.
- Provide disease prevention and treatment suggestions.




## 📄 License

This project is developed for educational and academic purposes.
