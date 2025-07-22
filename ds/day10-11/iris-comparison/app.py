import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from model_utils import get_models

st.set_page_config(page_title="Iris Classifier Comparison", layout="centered")
st.title("🌸 Iris Classifier Comparison App")

iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = get_models()
model_name = st.sidebar.selectbox("Select Classifier", list(models.keys()))

model = models[model_name]
model.fit(X_train, y_train)
preds = model.predict(X_test)

acc = accuracy_score(y_test, preds)
report = classification_report(y_test, preds, target_names=target_names, output_dict=True)
cm = confusion_matrix(y_test, preds)

st.subheader(f"🔍 Results for {model_name}")
st.metric(label="Accuracy", value=f"{acc*100:.2f}%")

st.write("### 🧾 Classification Report")
df_report = pd.DataFrame(report).transpose()
st.dataframe(df_report.style.format({"precision": "{:.2f}", "recall": "{:.2f}", "f1-score": "{:.2f}"}))

st.write("### Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="PuBu", xticklabels=target_names, yticklabels=target_names, ax=ax)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title(f"{model_name} Confusion Matrix")
st.pyplot(fig)
