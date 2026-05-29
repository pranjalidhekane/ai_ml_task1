Health Prediction Application
1. Project Overview

The Health Prediction Application is a Streamlit-based web application that allows users to manage patient health records and predict possible health risks using blood test results.

The application collects patient information such as:

Full Name
Date of Birth
Email Address
Glucose Level
Haemoglobin Level
Cholesterol Level

After entering valid patient data, the application sends the blood test values to the OpenRouter AI API, which analyzes the results and generates a health prediction. The prediction is automatically stored in the Remarks field.

The application supports complete CRUD (Create, Read, Update, Delete) operations and stores patient records in a SQLite database.

2. Technologies Used
Frontend
Streamlit
Backend
Python
Database
SQLite
AI Integration
OpenRouter API
GPT Model
Libraries
streamlit
pandas
requests
python-dotenv
sqlite3
3. Installation Steps
Clone Repository
git clone <repository-url>
cd ai_ml_task1
Create Virtual Environment
python -m venv .venv
Activate Virtual Environment

Windows:

.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app.py

The application will open in your browser automatically.

4. API Setup

This project uses OpenRouter API for AI-based health prediction.

Create .env File

Create a file named .env in the project root directory.

Example:

OPENROUTER_API_KEY=your_openrouter_api_key
Install dotenv
pip install python-dotenv
Load Environment Variable

The application reads the API key securely using:

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
Security Note

API keys, passwords, and other sensitive credentials are excluded from GitHub using .gitignore.

5. Screenshots
Add Patient Screen

Insert screenshot here.

View Patient Records

Insert screenshot here.

Update Patient Record

Insert screenshot here.

Delete Patient Record

Insert screenshot here.

AI Prediction Output

Insert screenshot here.

6. Features
CRUD Operations
Add new patient records
View patient records
Update patient information
Delete patient records
Data Validation
Email validation
Date of birth validation
Numeric validation for blood test values
AI Prediction
Predicts possible health risks
Automatically generates remarks
Database Storage
Stores records permanently using SQLite
User-Friendly Interface
Simple and clean Streamlit interface
7. Future Improvements
User Authentication and Login System
Search and Filter Patient Records
Export Data to CSV or Excel
Dashboard with Health Analytics
Disease Risk Scoring System
Cloud Database Integration
Medical Report Upload Feature
Deployment on Streamlit Cloud or Render
Enhanced AI-based Diagnosis Suggestions
Author

Pranjali Dhekane

Health Prediction Application developed as part of an AI/ML assessment project.
