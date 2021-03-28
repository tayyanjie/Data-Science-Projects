# Stroke Prediction
`healthcare-dataset-stroke-data.csv` contains the dataset obtained from [Kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset).

The `Stroke-Prediction.ipynb` notebook contains the code for the models that are trained on the dataset to predict stroke based on the features listed below.

## Features
**Categorical Features include:**
1. Gender
2. Hyptertension
3. Heart Disease
4. Ever Married
5. Work Type
6. Residence Type
7. Smoking Status

**Numerical Features include:**
1. Age
2. Average Glucose Level
3. BMI

## Method
Traditional Machine Learning Methods including Support Vector Machines (SVM), Logistic Regression, Random Forest and K Nearest Neighbors (KNN) have been used to create models to predict stroke based on the above features.

## Evaluation Metric
For stroke prediction, it is essential that individuals that are likely to obtain stroke will be predicted to get stroke. Hence, it is of importance to minimize False Negatives. Hence, recall is used as the main evaluation metric. 
<p align="center">
  <img src="http://www.sciweavers.org/upload/Tex2Img_1616630072/render.png">
</p>

where TP represents True Positives and FN represents False Negatives.
