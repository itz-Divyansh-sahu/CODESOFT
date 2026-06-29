# **🌸 Iris Flower Classification using Machine Learning**
### This project demonstrates a complete machine learning pipeline for classifying iris flowers into three species based on physical measurements. The dataset is simple yet powerful for understanding classification concepts, preprocessing, and model evaluation.

# <br> **📌 Problem Statement**
### Given measurements of iris flowers:
- ***Sepal Length***
- ***Sepal Width***
- ***Petal Length***
- ***Petal Width***

### The goal is to predict the species:
- ***Setosa***
- ***Versicolor***
- ***Virginica***
### This is a multi-class classification problem.

# <br> **📂 Dataset**
<a href="https://www.kaggle.com/datasets/arshid/iris-flower-dataset">Kaggle Direct Link</a>

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("arshid/iris-flower-dataset")

print("Path to dataset files:", path)
```
## <p align="center"> OR</p>
```python
df = pd.read_csv('IRIS.csv')
```
# <br> **📁 Project Structure**
```structure
Iris-Flower-Classification/
|- README.md
|- requirement.txt
|- IRIS.csv
|- iris.ipynb
```
# <br> **🧠 Machine Learning Models Used**
### The following models were trained and compared:
- ***K-Nearest Neighbors***
- ***Logistic Regression***
- ***Support Vector Machine***
### All models achieved high accuracy due to the strong separability of the dataset.

# <br> **🚀 Technologies Used**
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
cd CODESOFT/Data Science/Iris-Flower-Classification/
```
### Run the Jupyter Notebook:
```
iris.ipynb
```

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
