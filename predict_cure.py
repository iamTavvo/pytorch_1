import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# loading dataset
dataset = pd.read_csv("cancer.csv")

x = dataset.drop(columns=["diagnosis(1=m, 0=b)"])
y = dataset["diagnosis(1=m, 0=b)"]

# scale features
scaler = StandardScaler()
x = scaler.fit_transform(x)

# split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# define model
model = MLPClassifier(hidden_layer_sizes=(256, 256),
                      max_iter=1300,
                      activation="relu",
                      solver="adam",
                      verbose=True,
                      tol=0.0,
                      early_stopping=False)

# training model
model.fit(x_train, y_train)

# evaluate
y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# check iterations & loss
print("Final loss:", model.loss_)
print("Iterations run:", model.n_iter_)
