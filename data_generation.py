import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 500 days of "synthetic" student data
n_days = 500
data = {
    'Sleep_Hours': np.random.uniform(4, 9, n_days),
    'Study_Hours': np.random.uniform(1, 10, n_days),
    'Screen_Time': np.random.uniform(2, 12, n_days),
    'Exercise_Mins': np.random.choice([0, 30, 60], n_days),
    'Is_Weekend': np.random.choice([0, 1], n_days, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Logic for Target Variable (Productivity)
# High study + good sleep = High Productivity
# High screen time + low sleep = Low Productivity
def calculate_productivity(row):
    score = (row['Study_Hours'] * 0.5) + (row['Sleep_Hours'] * 0.3) - (row['Screen_Time'] * 0.2)
    if score > 4.5: return 2 # High
    if score > 2.5: return 1 # Medium
    return 0 # Low

df['Productivity_Label'] = df.apply(calculate_productivity, axis=1)

# Save to CSV
df.to_csv('student_productivity_data.csv', index=False)
print("Phase 1 Complete: Dataset 'student_productivity_data.csv' created!")