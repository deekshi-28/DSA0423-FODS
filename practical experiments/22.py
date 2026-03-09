import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/shopping_data.csv")

# Encode categorical variables
le_device = LabelEncoder()
le_purchase = LabelEncoder()

data['device_type'] = le_device.fit_transform(data['device_type'])
data['purchase'] = le_purchase.fit_transform(data['purchase'])

# Features and target
X = data[['age','income','browsing_duration','device_type']]
y = data['purchase']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Predict for test data
predictions = model.predict(X_test)

print("Predictions:", predictions)

# Predict for new customer
new_customer = pd.DataFrame(
    [[29,40000,12,le_device.transform(['Mobile'])[0]]],
    columns=['age','income','browsing_duration','device_type']
)

result = model.predict(new_customer)

print("Will the customer purchase?:", le_purchase.inverse_transform(result))