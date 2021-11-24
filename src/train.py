import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import pickle

project_path = ""

data_file_name = "data/auto-mpg.csv"

model_path = "data/models/"
model_file_name = 'trained_model.sav'

# load the data
df = pd.read_csv(project_path + data_file_name, sep=';')

# split data in training and test data
data_array = df.values
X = data_array[:, 1:5]
Y = data_array[:, 0]

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=test_size, random_state=seed)

# Fit the model on training set
model = LinearRegression()
model.fit(X_train, Y_train)

# save the model to disk
pickle.dump(model, open(project_path + model_path + model_file_name, 'wb'))
