from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(values, contamination=0.1):
    try:
        data = np.array(values).reshape(-1, 1)
        model = IsolationForest(contamination=contamination)
        predictions = model.fit_predict(data)
        return predictions
    except Exception as e:
        return {"error": str(e)}
