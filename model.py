import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import os

# 1. Use the EXACT file name we found earlier
import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_productivity_data.csv")
if os.path.exists(file_path):
    # Load data
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully for modeling!")

    # 2. Split features (X) and target (y)
    # Note: Updated 'Productivity_Level' to 'Productivity_Label' to match your CSV
    X = df.drop('Productivity_Label', axis=1) 
    y = df['Productivity_Label']

    # 3. Split into Training and Testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Initialize and Train Model
    print("Training the Random Forest... please wait.")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Make Predictions
    predictions = model.predict(X_test)

    # 6. Print Results
    print("\n" + "="*30)
    print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2%}")
    print("="*30)
    print("\nClassification Report:\n", classification_report(y_test, predictions))

else:
    print(f"❌ Error: The file '{file_path}' was not found. Please double-check the folder.")