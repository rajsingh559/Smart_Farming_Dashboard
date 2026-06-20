# 🌱 Smart Farming Dashboard

A comprehensive agriculture analytics platform built using **Django**, **Machine Learning**, and **Tableau Dashboards** to help farmers make data-driven decisions for improving crop productivity and farm management.

---

## 📌 Project Overview

Smart Farming Dashboard is a web-based agricultural analytics system that integrates:

* Farmer Management
* Crop Recommendation
* Yield Prediction
* Interactive Tableau Dashboards
* User Authentication
* Feedback Management
* Admin Monitoring

The platform enables farmers and administrators to visualize agricultural insights and leverage machine learning predictions for better decision-making.

---

## 🚀 Features

### 🔐 Authentication System

* User Registration
* User Login
* Logout
* Role-Based Access Control
* Farmer and Admin Roles

### 👤 User Profile Management

* Update Profile Information
* Farm Location Management
* Farm Size Details
* Preferred Crop Information

### 📊 Tableau Dashboard Integration

#### Crop Analysis Dashboard

* Crop Production Analysis
* Region-wise Crop Distribution
* Seasonal Crop Trends

#### Weather Analytics Dashboard

* Rainfall Trends
* Temperature Analysis
* Humidity Monitoring

#### Yield Prediction Dashboard

* Predicted Yield Metrics
* Production Forecasts
* Analytical Insights

#### Farmer Statistics Dashboard

* Farmer Registrations
* Farm Distribution
* Crop Preferences
* Agricultural Demographics

### 🤖 Machine Learning Module

#### Crop Recommendation System

Input Parameters:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* Soil pH
* Rainfall

Output:

* Recommended Crop

Algorithm:

* Random Forest Classifier

---

#### Yield Prediction System

Input Parameters:

* Farm Size
* Crop Type
* Rainfall
* Temperature
* Soil Parameters

Output:

* Predicted Crop Yield

Algorithm:

* Random Forest Regressor

---

### 📧 Notification System

* Email Notifications
* Prediction Alerts
* Recommendation Updates
* Admin Announcements

---

### ⭐ Feedback System

* Submit Feedback
* 5-Star Ratings
* Feedback Management
* User Satisfaction Tracking

---

## 🛠️ Technology Stack

### Backend

* Django
* Django REST Framework
* Python

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* SQLite (Development)
* PostgreSQL (Production)

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Dashboard & Visualization

* Tableau Public

### Deployment

* Render
* Railway
* AWS (Optional)

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
smart_farming/
│
├── accounts/
├── dashboard/
├── recommendations/
├── predictions/
├── reports/
├── notifications/
├── feedback/
│
├── templates/
├── static/
├── media/
│
├── docs/
│   └── PLAN.md
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📈 Tableau Dashboards

### Crop Analysis

https://public.tableau.com/views/Smart_Farming_DashboardCrop_Analysis/Dashboard1

### Weather Analytics

https://public.tableau.com/views/Smart_Farming_Dashboard/Dashboard2

### Yield Prediction

https://public.tableau.com/views/Smart_Farming_DashboardYield_Prediction/Dashboard3

### Farmer Statistics

https://public.tableau.com/views/Smart_Farming_DashboardFarmer_Statistics/Dashboard4

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd smart-farming-dashboard
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

---

## 🌐 Access Application

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 📊 Future Enhancements

* Real-Time IoT Sensor Integration
* SMS Notifications
* WhatsApp Notifications
* AI Chatbot for Farmers
* Weather API Integration
* Satellite Image Analysis
* Mobile Application
* Cloud-Based Analytics

---

## 👨‍💻 Author

**Raj Singh**

Computer Science and Data Science Undergraduate

---

## 📜 License

This project is developed for academic and educational purposes.
