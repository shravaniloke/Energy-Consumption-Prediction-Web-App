# 🔌 Energy Consumption Prediction Web App

This project is an end-to-end **Machine Learning web application** that predicts **energy consumption of buildings** based on building characteristics, usage patterns, and environmental factors.

The application uses a **Random Forest Regressor** for prediction and is deployed using **Flask** with a clean, card-based frontend UI.

---

## 📌 Project Overview

Energy consumption depends on multiple factors such as:
- Type of building
- Size of the building
- Number of occupants
- Number of appliances
- Temperature conditions
- Day of the week

This project takes these inputs from the user and predicts the **expected energy consumption**.

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor  
- **Problem Type:** Regression  
- **Evaluation Metrics:**
  - R² Score
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)

### Model Performance
- **R² Score:** ~0.97  
- **MAE:** ~94 units  
- **RMSE:** ~119 units  

These results indicate a strong and reliable prediction model.

---

## 🌐 Web Application Features

- User-friendly form to enter building details
- Dropdowns for categorical inputs
- Clean card-style UI
- Real-time energy consumption prediction
- Model loaded from a `.pkl` file (no retraining on each request)

---

## 🧾 User Inputs

- Building Type (Residential / Commercial / Industrial)
- Square Footage
- Number of Occupants
- Number of Appliances Used
- Average Temperature (°C)
- Day of Week (Weekday / Weekend)

---

## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- Scikit-learn
- Random Forest Regressor

### Web Development
- Flask
- HTML
- CSS

---

## 📂 Project Structure
Energy-Consumption-Predictor/
│

├── app.py

├── energy_model.pkl

├── README.md

│
└── templates/

└── index.html

---

## 🚀 How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/energy-consumption-predictor.git

2. Install dependencies:
   pip install flask pandas scikit-learn

3. Run the Flask app:
   python app.py

4. Open your browser and go to:
   http://127.0.0.1:5000/

---

📈 Future Improvements

- Add input validation and error handling
- Display model metrics on UI
- Store prediction history
- Deploy the app online (Render / Railway)
- Add data visualization

---

## Screenshot

<img width="1919" height="965" alt="image" src="https://github.com/user-attachments/assets/b066d23b-b76f-4243-86c5-0136799bfdb8" />

---
👩‍💻 Author

Shravani Loke
Machine Learning & Web Development Enthusiast
