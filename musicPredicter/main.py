# (1) Import the data
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
# (2) Prepare/Clean the data
# Separate the columns into input and output
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# (3) Split the data into training/test sets
# train_test_split, splits the data into training and testing sets
# The first arg 'X' is the input data and second arg 'y' is the output
# train and test are split correctly because of their naming convention
# not the order they are listed in
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# (4) Create a model
# DecisionTreeClassifier() builds a tree-like
# model of decisions and their possible consequences
model = DecisionTreeClassifier()

# (5) Train the model
# fit() tells the model to learn from the data you 
# provided where first arg is input and second arg
# is output
model.fit(X_train,y_train)

# (6) Make predictions
# predict(), takes 2d array
# inside the array each elemenet is an array where
# first element is the input and second is the 
# corresponding output
predictions = model.predict(X_test)

# (7) Evaluate and improve
# See how well the ml algorithm is able to predict
score = accuracy_score(y_test,predictions)
# The score will be printed from 0 - 1 where 0 is 0 %
# accuarcy and 1 is 100 % accuracy in the prediction
print(score)