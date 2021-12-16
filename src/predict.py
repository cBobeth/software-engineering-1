import pandas as pd
from sklearn import model_selection
import pickle

project_path = ""

data_file_name = "data/auto-mpg.csv"

model_path = "data/models/"
model_file_name = 'trained_model.sav'

# load the data
df = pd.read_csv(project_path + data_file_name, sep=';')

# split data in training and test data
data_array = df.values
X = data_array[:, 1:6]
Y = data_array[:, 0]

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=test_size, random_state=seed)

# load the model from disk
loaded_model = pickle.load(
    open(project_path + model_path + model_file_name, 'rb'))

# overall scoring of test data
score_result = loaded_model.score(X_test, Y_test)
print(f"\nTrained model scores with score = {score_result:4.3f} on test data")

# some predictions of test data
Y_pred_test = loaded_model.predict(X_test)

# for y_pred, y_meas in zip(Y_pred_test, Y_test):
#    print(f" prediction <--> measured = {y_pred:5.3f} <--> {y_meas:5.3f},"\
#          f"      ratio = {y_pred/y_meas:4.2f}")

print(f"\nminimal ratio = {min(Y_pred_test/Y_test):5.3f}")
print(f"\nmaximal ratio = {max(Y_pred_test/Y_test):5.3f}")
