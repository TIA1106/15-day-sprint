import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from model_utils import load_data, train_model
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="❤️ Heart Disease Classifier", layout="centered")
st.title("❤️ Heart Disease Prediction App")

model_name = st.selectbox("🔍 Choose a Classifier", ["Logistic Regression", "KNN", "Random Forest", "SVM"])

X_train, X_test, y_train, y_test = load_data()
model = train_model(model_name, X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
st.metric("🎯 Accuracy", f"{acc*100:.2f}%")

st.subheader("📊 Confusion Matrix")
fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=ax, cmap="Blues")
st.pyplot(fig)

st.subheader("📋 Classification Report")
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.dataframe(report_df.style.background_gradient(cmap="BuGn"))
