
# Zomato Restaurant Rating Prediction

## Project Overview
This project predicts restaurant ratings using Machine Learning and a Flask-based web application.

The project uses the Zomato restaurant dataset and an Extra Trees Regression model to estimate restaurant ratings based on restaurant-related features.

## Technologies Used
- Python 3.12
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Machine Learning

## Machine Learning Algorithm
Extra Trees Regressor with 120 estimators.

## Input Features
1. Online Order
2. Table Booking
3. Votes
4. Location
5. Restaurant Type
6. Cuisines
7. Average Cost
8. Menu Item

## Project Structure

```text
Zomato-Rating-Prediction/
│
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
├── Zomato_df.csv
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

## Installation and Setup

1. Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate into the project folder.

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the environment on Windows.

```bash
venv\Scripts\activate
```

5. Install dependencies.

```bash
pip install -r requirements.txt
```

6. Run the application.

```bash
python app.py
```

7. Open your browser.

```text
http://127.0.0.1:5000
```

## Project Objective
To develop a web-based machine learning application that estimates restaurant ratings using restaurant-related input features.

## Disclaimer
Predicted ratings are machine learning estimates and may differ from actual restaurant ratings.

## Academic Project
Developed for educational and academic purposes.

