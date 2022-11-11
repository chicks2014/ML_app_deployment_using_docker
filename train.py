import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle

df = pd.read_csv("online_sales.csv")

print(df.shape)

print(df.head())

print(df.converted.value_counts())

X = df.drop("converted", axis=1)
y = df["converted"]

print(f"X.shape={X.shape}, y.shape={y.shape}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123, stratify=y
)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

logres = LogisticRegression(class_weight="balanced").fit(X_train, y_train)

print(logres.score(X_test, y_test))

pred = logres.predict(X_test)

print(classification_report(y_test, pred, target_names=["Non-converted", "Converted"]))

print(confusion_matrix(y_test, pred))

# export model
pickle_out = open("logres.pkl", "wb")
pickle.dump(logres, pickle_out)
pickle_out.close()

# import model
pickle_in = open("logres.pkl", "rb")
model = pickle.load(pickle_in)

print("Prediction: ")
print(model.predict([[45, 0, 5]])[0])

# group data
df_test = pd.read_csv("test_data.csv")
print(df_test.head())
predictions = model.predict(df_test)
print("List of predictions: ")
print(list(predictions))
