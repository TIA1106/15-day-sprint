import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def load_data():
    df = pd.read_csv("dataset.csv")
    df = df.drop_duplicates()
    X = df.drop("target", axis=1)
    y = df["target"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def train_model(name, X_train, y_train):
    if name == "Logistic Regression":
        model = LogisticRegression()
    elif name == "KNN":
        model = KNeighborsClassifier()
    elif name == "Random Forest":
        model = RandomForestClassifier()
    else:
        model = SVC()

    model.fit(X_train, y_train)
    return model
