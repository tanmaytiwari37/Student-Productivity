# 🎓 Student Productivity Predictor (ML)

> A machine learning project that predicts student productivity (Low / Medium / High) based on daily habits like sleep, study, screen time, and exercise.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

---

## ✨ About

This project explores how everyday habits affect productivity using a **Random Forest classifier**. It generates synthetic student data, analyzes correlations between lifestyle factors, and trains a model to predict productivity levels.

Built as a self-driven ML project to practice **the full machine learning workflow** — from data generation to evaluation.

## 🎯 What It Does

- 📊 **Generates** a synthetic dataset of 500 days of student habits
- 🔥 **Analyzes** correlations between sleep, study, screen time, and productivity (heatmap)
- 🤖 **Trains** a Random Forest classifier to predict productivity (Low / Medium / High)
- 📈 **Evaluates** the model with accuracy and classification reports

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** — data manipulation
- **NumPy** — random data generation
- **Matplotlib + Seaborn** — correlation heatmap visualization
- **scikit-learn** — Random Forest model + evaluation metrics

## 📁 Project Structure
```
Student_Productivity_ML/
├── data_generation.py            # Creates 
├── analysis.py                   # Generates 
├── model.py                      # Trains and 
├── student_productivity_data.csv # Generated dataset
├── correlation_chart.png         # Output heatmap
├── Project_Report.pdf            # Detailed project report
└── README.md
```
## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.10
```

### Installation

```bash
# Clone the repo
git clone https://github.com/tanmaytiwari37/Student_Productivity_ML.git
cd Student_Productivity_ML

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run

The project runs in **3 phases**:

```bash
# Phase 1: Generate dataset (optional — CSV already provided)
python data_generation.py

# Phase 2: Explore data with correlation heatmap
python analysis.py

# Phase 3: Train and evaluate the model
python model.py
```

⚠️ Run all commands from the **project root folder**, not from a subfolder — paths are relative.

## 📊 Dataset

The synthetic dataset simulates 500 days of student habits:

| Feature | Type | Range | Meaning |
|---|---|---|---|
| `Sleep_Hours` | float | 4 – 9 | Hours slept |
| `Study_Hours` | float | 1 – 10 | Hours studied |
| `Screen_Time` | float | 2 – 12 | Hours on screen |
| `Exercise_Mins` | int | {0, 30, 60} | Minutes exercised |
| `Is_Weekend` | int | {0, 1} | Weekend flag |
| `Productivity_Label` | int | {0, 1, 2} | **Target**: 0=Low, 1=Med, 2=High |

### How the Label Is Generated

```python
score = (Study_Hours × 0.5) + (Sleep_Hours × 0.3) - (Screen_Time × 0.2)

if score > 4.5:  Label = 2 (High)
elif score > 2.5: Label = 1 (Medium)
else:             Label = 0 (Low)
```

## 🧠 The ML Pipeline
```
Generate data  →  data_generation.py
↓
Explore        →  analysis.py (correlation heatmap)
↓
Split          →  train_test_split (80/20)
↓
Train          →  RandomForestClassifier(n_estimators=100)
↓
Predict        →  model.predict(X_test)
↓
Evaluate       →  accuracy + classification_report
```
## 📈 Sample Output

### Correlation Heatmap (`analysis.py`)

The heatmap reveals which factors most strongly correlate with productivity. Study hours and sleep show **positive correlation** with productivity, while screen time shows **negative correlation**.

### Model Performance (`model.py`)
```
==============================
Model Accuracy: 98.00%
Classification Report:
precision    recall  f1-score   support
0       0.96      1.00      0.98        24
1       0.98      0.96      0.97        45
2       1.00      1.00      1.00        31
```
⚠️ **Why accuracy is so high:** The dataset is synthetic and follows a deterministic formula. The model essentially "learns" the rule used to generate the labels. On real-world data, accuracy would be lower and more meaningful.

## 🧠 What I Learned

- **End-to-end ML workflow** — from data generation to evaluation
- **Random Forest** — how ensemble learning works under the hood
- **Train/test split** — why we hold out data for honest evaluation
- **Correlation analysis** — using heatmaps to spot feature relationships
- **Classification metrics** — accuracy vs. precision vs. recall vs. F1
- **Synthetic data trap** — high accuracy on generated data isn't real proof of skill

## 🔭 Roadmap

- [ ] Replace synthetic data with a **real student dataset** (e.g., Kaggle)
- [ ] Add noise to the label generation to make the problem realistic
- [ ] Compare multiple models (Logistic Regression, XGBoost, SVM)
- [ ] Add **cross-validation** instead of single train/test split
- [ ] Visualize feature importance from the Random Forest
- [ ] Build a **Streamlit app** to predict productivity from user inputs

## ⚠️ Known Limitations

- **Synthetic data** — productivity labels are computed from a fixed formula, so the model learns that formula instead of real-world patterns
- **No cross-validation** — single train/test split can give optimistic accuracy
- **No hyperparameter tuning** — uses default Random Forest settings

## 👤 About Me

**Tanmay Tiwari** — 1st-year B.Tech Aerospace Engineering, VIT Bhopal

- 🌐 GitHub: [@tanmaytiwari37](https://github.com/tanmaytiwari37)
- 📧 itanmaytiwari37@gmail.com
- 🎯 Currently exploring: ML for engineering, data analysis, and end-to-end Python projects

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and learn from.

---

<sub>Built as a self-study project to learn the full ML pipeline using scikit-learn.</sub>