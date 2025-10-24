import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

X = pd.DataFrame({'x':[1,2,3,4,5]})
y = pd.Series([2,4,6,8,10])

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, 'smv_predictor_v1.joblib')
print("Model trained and saved!")
