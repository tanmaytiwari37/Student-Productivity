import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- UPDATED FILE NAME ---
import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_productivity_data.csv")
if os.path.exists(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    print("✅ File loaded successfully!")
    
    print("\n--- Data Preview ---")
    print(df.head())

    # Create Correlation Heatmap
    plt.figure(figsize=(10, 6))
    
    # We use numeric_only=True to ensure it only calculates numbers
    correlation_matrix = df.corr(numeric_only=True)
    
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('What factors affect Productivity?')
    
    # Save and Show
    plt.savefig('correlation_chart.png')
    print("\n✅ Analysis Complete: 'correlation_chart.png' saved in your folder.")
    plt.show()

else:
    print(f"❌ Still can't find it! Check if the filename in the code matches the folder exactly.")