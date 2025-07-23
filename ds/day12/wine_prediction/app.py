import streamlit as st
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np
import pandas as pd

# Load and prepare data
wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
class_names = wine.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(probability=True)
}

for model in models.values():
    model.fit(X_train_scaled, y_train)

st.title("🍷 Wine Class Prediction App")

st.sidebar.header("🔧 Choose a Model")
selected_model_name = st.sidebar.selectbox("Model", list(models.keys()))
selected_model = models[selected_model_name]

st.sidebar.header("🎛️ Enter Feature Values")

input_data = []
for feature in feature_names:
    min_val = float(np.min(X[:, feature_names.index(feature)]))
    max_val = float(np.max(X[:, feature_names.index(feature)]))
    default_val = float(np.mean(X[:, feature_names.index(feature)]))
    val = st.sidebar.slider(feature, min_val, max_val, default_val)
    input_data.append(val)

input_np = np.array(input_data).reshape(1, -1)
input_scaled = scaler.transform(input_np)

prediction = selected_model.predict(input_scaled)[0]
proba = selected_model.predict_proba(input_scaled)[0]

st.subheader("🎯 Prediction")
st.write(f"**Predicted Class:** {class_names[prediction]}")

st.subheader("📈 Prediction Probabilities")
df_proba = pd.DataFrame(proba.reshape(1, -1), columns=class_names)
st.bar_chart(df_proba.T)
