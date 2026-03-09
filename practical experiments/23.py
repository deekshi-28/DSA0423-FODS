import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/loan_data.csv")


# Encode target variable
le = LabelEncoder()
data['risk'] = le.fit_transform(data['risk'])

# Features and target
X = data[['income','credit_score','debt_income_ratio','employment_duration']]
y = data['risk']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

# Train CART model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Predictions for test data
predictions = model.predict(X_test)

print("Predicted Risk Values:", predictions)

# Predict for a new applicant
new_applicant = pd.DataFrame(
    [[42000,670,30,5]],
    columns=['income','credit_score','debt_income_ratio','employment_duration']
)
result = model.predict(new_applicant)

print("Predicted Credit Risk:", le.inverse_transform(result))