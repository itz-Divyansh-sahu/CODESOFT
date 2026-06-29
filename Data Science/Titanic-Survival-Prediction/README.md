# **About the Project**
### The sinking of the RMS Titanic is one of the most well-known maritime disasters in history. This project uses the Titanic dataset to build a classification model capable of predicting passenger survival.
### The goal is to analyze passenger information such as age, gender, ticket class, fare, family size, and embarkation port to determine the likelihood of survival.

# <br> **Objectives**
- ### Perform data cleaning and preprocessing
- ### Handle missing values
- ### Explore and visualize the dataset
- ### Engineer meaningful features
- ### Train and compare multiple machine learning models
- ### Evaluate model performance
- ### Predict passenger survival accurately

# <br> **📂 Dataset**
<a href="https://www.kaggle.com/datasets/yasserh/titanic-dataset">Kaggle Direct Link</a>

```python
import kagglehub
# Download latest version
path = kagglehub.dataset_download("yasserh/titanic-dataset")
print("Path to dataset files:", path)
```
## <p align="center"> OR</p>
```python
df = pd.read_csv('titanic-Dataset.csv')
```
# <br> **📁 Project Structure**
```structure
TITANIC SURVIVAL PREDICTION/
|- README.md
|- requirement.txt
|- titanic-dataset.csv
|- titanic.ipynb
```
# <br> **🛠 Technologies Used**
- ***Python*** 
- ***Pandas*** 
- ***NumPy*** 
- ***Matplotlib*** 
- ***Seaborn*** 
- ***Scikit-learn*** 
- ***Jupyter Notebook***

# <br> 🚀 Getting Started
## Prerequisites
```
pip install -r requirements.txt
```
## Installation

### Clone the repository:
```
git clone https://github.com/itz-Divyansh-sahu/CODESOFT.git
```
### Navigate to the project directory:
```
cd CODESOFT/Data Science/Titanic-Survival-Prediction/
```
### Run the Jupyter Notebook:
```
titanic.ipynb
```

# <br> **🤖 Machine Learning Models**
### Models that can be trained include:
- ***Logistic Regression***
- ***K-Nearest Neighbors (KNN)***
- ***Naive Bayes (NB)***
- ***Decision Tree***
- ***Support Vector Machine (SVM) 👈(High Accuracy)***
<br></br>

# **📈 Model Evaluation**
- ***Accuracy Score***
- ***Confusion Matrix***
- ***Precision***
- ***Recall***
- ***F1 Score***

# <br> **📜 License**
***This project is licensed under the MIT License.***

# <br> 🤝 Contributing
**Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.**

# <br> 👨‍💻 Author
## Divyansh Sahu
### Machine Learning Enthusiast | Python Developer | Data Science Learner
+ GitHub: https://github.com/itz-Divyansh-sahu
+ LinkedIn: https://linkedin.com/in/coder-divyansh-sahu

***⭐ If you found this project useful, consider giving it a star on GitHub!***
**It helps others discover the project and motivates future improvements.❤️**

***<p align="center">@divyansh_sahu</p>***