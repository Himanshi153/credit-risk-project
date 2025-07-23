# 💳 Credit Risk Prediction App using Random Forest and Streamlit

A complete end-to-end Machine Learning project that predicts **whether a person is creditworthy or not**, using financial and personal attributes.
Built with by [Himanshi Rathore](https://github.com/himanshi-rathore)  
📍 Streamlit web app | 📊 Random Forest Model | 📁 EDA + Visualizations

## 🔍 Project Objective
The goal of this project is to analyze the **German Credit dataset**, train a robust machine learning model, and make credit risk predictions via a simple **web application**.
> "Will this person be able to repay the loan or not?"

## 🚀 Live Demo
👉 _To be added after deployment on Streamlit Cloud_  
(_Let me know, I can help with this too_)

## 📁 Project Structure
credit-risk-project/
├── app.py # Streamlit web app
├── credit_model.pkl # Trained ML model (Random Forest)
├── convert_to_csv.ipynb #Convert .data to .csv
├── training_notebook.ipynb #EDA + Model Training
├── requirements.txt #Python dependencies

## 📊 Features of the App
- 📥 Upload or input customer details
- 🔍 Predict creditworthiness instantly
- 📈 Visual feedback on model prediction
- ⚙️ Backend powered by Random Forest Classifier

## 🔢 Input Features Used
- Checking Account Status
- Duration of Credit (in months)
- Credit History
- Purpose of Credit
- Credit Amount
- Savings Account / Bonds
- Present Employment Since
- Installment Rate (% of income)
- Personal Status and Sex
- Other Debtors / Guarantors
- Present Residence Since
- Property Type
- Age
- Housing
- Number of Existing Credits
- Job
- Number of People Liable
- Telephone Availability
- Foreign Worker (Yes/No)

## 🧪 Exploratory Data Analysis (EDA)
Performed using `pandas`, `matplotlib`, and `seaborn`:
- ✔️ Checked missing values
- ✔️ Handled categorical encoding
- ✔️ Visualized distributions, outliers, and correlations
- ✔️ Split data into training/testing
- ✔️ Trained Random Forest with tuning

## 🛠️ Technologies Used
- 🐍 Python
- 📊 Pandas, Numpy, Seaborn, Matplotlib
- 🤖 Scikit-learn (RandomForestClassifier)
- 🌐 Streamlit (for web deployment)

##Dataset
Source: UCI German Credit Dataset
Contains 1000 rows × 21 columns
Binary Target Variable:
1 = Good Credit Risk
2 = Bad Credit Risk
