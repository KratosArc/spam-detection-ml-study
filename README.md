# 📧 SMS Spam Detection — ML Algorithm Comparison Study

## 🌐 Live Demo
👉 [Test the API here](https://spam-detector-api-srfp.onrender.com/docs)

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-orange)
![Status](https://img.shields.io/badge/Status-Complete-green)

## 📌 Overview
A machine learning project comparing **Naive Bayes**, 
**Logistic Regression**, and **KNN** algorithms on 
SMS spam detection using the UCI SMS Spam Collection dataset.

---

## 📊 Final Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| **Naive Bayes** 🥇 | 97.04% | 100% | 78% | 87.64% |
| Logistic Regression | 96.5% | 100% | 74% | 85.06% |
| KNN | 92.11% | 100% | 41.33% | 58.49% |

✅ **Winner: Naive Bayes** with highest F1 Score of 87.64%

---

## 📁 Project Structure
```
spam-detection-ml-study/
├── notebook/
│   └── spam_detection_comparison.ipynb
├── data/
│   └── spam.csv
├── images/
│   ├── class_distribution.png
│   ├── message_length.png
│   ├── confusion_matrices.png
│   └── model_comparison.png
├── models/
│   ├── naive_bayes_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── knn_model.pkl
│   └── tfidf_vectorizer.pkl
├── README.md
└── requirements.txt
```

---

## 🛠️ Libraries Used
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🚀 How to Run
1. Clone the repository
```bash
git clone https://github.com/Jiveshwar/spam-detection-ml-study.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Open the notebook
```bash
jupyter notebook notebook/spam_detection_comparison.ipynb
```

---

## 📈 Key Findings
- Spam messages are **2x longer** than ham messages
- All models achieved **100% Precision**
- Naive Bayes best suited for text classification
- KNN struggled with only **41% Recall**

---

## 👨‍💻 Author
**Jiveshwar Singh Rathore**  | Aspiring ML & GenAI Engineer  
[LinkedIn](https://www.linkedin.com/in/jiveshwarrathore/) |
