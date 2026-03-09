import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/fruit_data.csv")

# Encode categorical variables
le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

data['color'] = le_color.fit_transform(data['color'])
data['texture'] = le_texture.fit_transform(data['texture'])
data['type'] = le_type.fit_transform(data['type'])

# Features and target
X = data[['weight','color','texture']]
y = data['type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

# Prediction for new fruit
new_fruit = [[155, le_color.transform(['Red'])[0], le_texture.transform(['Smooth'])[0]]]
prediction = model.predict(new_fruit)

print("Predicted Fruit:", le_type.inverse_transform(prediction))

# Model accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,y_pred))