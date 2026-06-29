# **🎬 Movie Rating Prediction using Machine Learning**
### This project aims to predict the IMDb rating of Indian movies using machine learning techniques. The model learns from historical movie data such as genre, duration, director, actors, release year, and audience votes to estimate a movie's rating.
### The project demonstrates a complete machine learning workflow, including data preprocessing, feature engineering, model training, evaluation, and comparison of multiple regression algorithms.

# <br> **🎯 Objectives**
- ***Analyze and preprocess movie metadata.***
- ***Handle missing values and clean inconsistent data.***
- ***Perform feature engineering to improve model performance.***
- ***Train multiple regression models.***
- ***Compare model performance using regression metrics.***
- ***Identify the best-performing model for movie rating prediction.***


# <br> **📂 Dataset**
# Dataset: <a href="https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies">IMDb India Movies Dataset</a>

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("adrianmcmahon/imdb-india-movies")

print("Path to dataset files:", path)
```
## <p align="center"> OR</p>
```python
df = pd.read_csv('IMBb Movies India.csv')
```
# <br> **📁 Project Structure**
```structure
Iris-Flower-Classification/
|- IMDb Movies India.csv
|- movie.ipynb
|- README.md
|- requirement.txt
```
# <br> **🧠 Machine Learning Models Used**
### The following models were trained and compared:
- ***Linear Regression***
- ***Random Forest***
- ***XGBoost***

# <br> **🚀 Technologies Used**
- ***Python*** 
- ***Pandas*** 
- ***NumPy*** 
- ***Matplotlib*** 
- ***Seaborn*** 
- ***Scikit-learn*** 
- ***XGBoost***
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
cd CODESOFT/Data Science/Movie-Rating-Prediction/
```
### Run the Jupyter Notebook:
```
movie.ipynb
```

### Run all cells to reproduce the preprocessing, model training, and evaluation.

# <br> **📊 Model Evaluation**
- ***Mean Absolute Error (MAE)***
- ***Root Mean Squared Error (RMSE)***
- ***R² Score***

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