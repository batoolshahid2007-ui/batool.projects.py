import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

n_samples = 500

temperature = np.random.uniform(60, 110, n_samples)
vibration = np.random.uniform(2, 10, n_samples)

hours_to_failure = (
    1000
    - (5.5 * temperature)
    - (45 * vibration)
    + np.random.normal(0, 15, n_samples)
)

data = pd.DataFrame({
    "Temperature": temperature,
    "Vibration": vibration,
    "Hours_to_Failure": hours_to_failure
})

X = data[["Temperature", "Vibration"]]
y = data["Hours_to_Failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=" * 45)
print("        MACHINE FAILURE PREDICTION")
print("=" * 45)

print("\nModel Evaluation")
print("----------------")
print(f"Mean Absolute Error : {mae:.2f} hours")
print(f"R² Score            : {r2:.4f}")
print(f"Model Accuracy      : {r2 * 100:.2f}%")

print("\nModel Equation")
print("--------------")
print(
    f"Hours_to_Failure = {model.intercept_:.2f} "
    f"+ ({model.coef_[0]:.2f} × Temperature) "
    f"+ ({model.coef_[1]:.2f} × Vibration)"
)

new_sensor_data = pd.DataFrame(
    {
        "Temperature": [95.0],
        "Vibration": [7.5]
    }
)

predicted_life = model.predict(new_sensor_data)

print("\nLive Machine Prediction")
print("-----------------------")
print(f"Temperature : {new_sensor_data['Temperature'][0]:.1f} °C")
print(f"Vibration   : {new_sensor_data['Vibration'][0]:.1f} mm/s")
print(f"Predicted Remaining Life : {predicted_life[0]:.2f} hours")

print("\nProgram Executed Successfully.")
