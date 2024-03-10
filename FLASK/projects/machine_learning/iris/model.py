import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the csv file
data_frame = pd.read_csv('./assets/iris.csv')

print(data_frame.head())


# Select independent and dependent variables
x = data_frame[['Sepal_Length', 'Sepal_Width',
                'Petal_Length', 'Petal_Width']]  # Independent variables
y = data_frame['Species']  # Dependent variable

# Split the dataset into random train and test subsets
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=50)


# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Instiantiate the model
classifier = RandomForestClassifier()

# Fit  the model
classifier.fit(X_train, y_train)

# Make a pickle file of our model
pickle.dump(classifier, open('./assets/model.pkl', 'wb'))

