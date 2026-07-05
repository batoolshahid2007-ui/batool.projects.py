# Machine Failure Prediction Using Linear Regression

## Overview

This project demonstrates a simple **Machine Failure Prediction System** using **Python** and **Machine Learning**. A **Linear Regression** model is trained on synthetic machine sensor data to estimate the **remaining operating hours before machine failure**.

The model uses two important sensor parameters:

* Temperature (°C)
* Vibration (mm/s)

Based on these inputs, it predicts the machine's remaining useful life (RUL) in hours.

---

## Features

* Synthetic machine sensor data generation
* Data preprocessing using Pandas
* Train-test data splitting
* Linear Regression model training
* Model performance evaluation
* Mean Absolute Error (MAE) calculation
* R² Score (Model Accuracy)
* Live prediction using new sensor readings

---

## Technologies Used

* Python 3
* NumPy
* Pandas
* Scikit-learn

---

## Project Workflow

1. Generate synthetic machine sensor data.
2. Create a dataset containing temperature, vibration, and remaining life.
3. Split the dataset into training and testing sets.
4. Train a Linear Regression model.
5. Evaluate the model using MAE and R² Score.
6. Predict the remaining life of a machine using new sensor values.

---

## Dataset

The project generates a synthetic dataset with **500 samples**.

### Input Features

| Feature     | Description               |
| ----------- | ------------------------- |
| Temperature | Machine temperature in °C |
| Vibration   | Machine vibration in mm/s |

### Target

| Target           | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| Hours_to_Failure | Estimated remaining operating hours before machine failure |

---

## Project Structure

```text
Machine-Failure-Prediction/
│
├── machine_failure_prediction.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/machine-failure-prediction.git
```

Move into the project folder:

```bash
cd machine-failure-prediction
```

Install the required libraries:

```bash
pip install numpy pandas scikit-learn
```

---

## Running the Project

Execute the Python script:

```bash
python machine_failure_prediction.py
```

---

## Sample Output

```text
=============================================
        MACHINE FAILURE PREDICTION
=============================================

Model Evaluation
----------------
Mean Absolute Error : 12.58 hours
R² Score            : 0.9864
Model Accuracy      : 98.64%

Live Machine Prediction
-----------------------
Temperature : 95.0 °C
Vibration   : 7.5 mm/s
Predicted Remaining Life : 138.52 hours

Program Executed Successfully.
```

*Note: The exact values may vary because the dataset contains randomly generated sensor readings.*

---

## Applications

* Predictive Maintenance
* Smart Manufacturing
* Industrial Automation
* Equipment Health Monitoring
* Industry 4.0 Solutions
* Condition-Based Maintenance

---

## Future Improvements

* Use real industrial sensor data instead of synthetic data.
* Support multiple machine sensors such as pressure, humidity, current, and RPM.
* Compare multiple machine learning algorithms (Random Forest, Decision Tree, Support Vector Regression, XGBoost).
* Build an interactive web dashboard using Flask or Streamlit.
* Add real-time IoT sensor integration.
* Visualize predictions with graphs and charts.
* Save and reload trained models using Joblib.

---

## Requirements

* Python 3.8 or later
* NumPy
* Pandas
* Scikit-learn

Install all dependencies using:

```bash
pip install numpy pandas scikit-learn
```

---

## License

This project is released under the MIT License. You are free to use, modify, and distribute it with proper attribution.

---

## Author

**Batool Shahid**

If you found this project useful, consider giving the repository a ⭐ on GitHub.
