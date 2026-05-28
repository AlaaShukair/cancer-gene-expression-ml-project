# Cancer Type Prediction Using Gene Expression Data

##  Project Overview

This project uses machine learning techniques to classify cancer samples based on RNA-seq gene expression data. The workflow includes preprocessing, exploratory data analysis, feature selection, machine learning model comparison, hyperparameter tuning, and deployment using Streamlit.
##  Project Links

### GitHub Repository
https://github.com/AlaaShukair/cancer-gene-expression-ml-project

### Streamlit Prediction App
https://cancer-gene-expression-ml-project-apubdjabrpuoqoy5kgzzyt.streamlit.app/

## Key Features

✅ Bioinformatics and RNA-seq dataset  
✅ Multiclass cancer classification  
✅ Data preprocessing and missing value handling  
✅ Exploratory Data Analysis (EDA)  
✅ Feature selection using SelectKBest  
✅ Multiple machine learning models  
✅ Hyperparameter tuning with GridSearchCV  
✅ Streamlit web application deployment  

---

## Dataset Information

The dataset contains RNA-seq gene expression values where:
- Rows represent biological samples
- Columns represent gene expression features
- The target column represents cancer classes

The dataset originally contained missing target labels and missing numerical values, which were handled during preprocessing.

---

##  Machine Learning Pipeline

### Data Preprocessing
- Removed rows with missing target labels
- Filled missing numerical values using median imputation
- Checked for duplicate samples

### Exploratory Data Analysis
Visualizations included:
- Histograms
- Boxplots
- Scatter plots
- Correlation heatmaps
- Class distribution plots
  
  ## Feature Engineering

New statistical features were created, including mean gene expression and standard deviation, to capture additional patterns in the gene expression data.

### Feature Selection
SelectKBest with ANOVA F-test was used to select the top 100 most informative genes.

### Machine Learning Models
The following algorithms were trained and compared:
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

### Hyperparameter Tuning
GridSearchCV was applied to optimize the Random Forest model.

### Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

##  Streamlit Web Application

The project was deployed using Streamlit to allow real-time cancer class prediction based on selected gene expression values.

---

##  Project Structure
cancer-gene-expression-ml-project/
│
├── app.py
├── Cancer_Gene_Expression_ML_Project.ipynb
├── cancer_model.pkl
├── scaler.pkl
├── selector.pkl
├── label_encoder.pkl
├── selected_features.pkl
├── requirements.txt
└── README.md

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

##  Dataset Source

RNA-Seq Gene Expression Dataset Multi-Class Cancer

https://www.kaggle.com/datasets/udayraman/rna-seq-gene-expression-datase-multi-class-cancer

---

##  How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Future Improvements

- Add explainable AI methods such as SHAP or LIME
- Improve class balancing techniques
- Add prediction confidence scores
- Explore deep learning approaches for RNA-seq analysis

---

##  Author

Alaa Shukair
