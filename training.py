# training.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

if __name__ == "__main__":
    # Generate synthetic data
    df = pd.DataFrame({
        'feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
        'feature2': [1, 2, 3, 4, 5],
        'label': [0, 1, 0, 1, 0]
    })

    X = df[['feature1', 'feature2']]
    y = df['label']

    # Train simple logistic regression
    model = LogisticRegression()
    model.fit(X, y)

    # Save the model locally
    os.makedirs('/opt/ml/model', exist_ok=True)
    joblib.dump(model, '/opt/ml/model/model.joblib')

    print("Training completed. Model saved to /opt/ml/model/")
