import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("data.csv")

X = data["skills"]
y = data["role"]

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

def predict_role(skills):
    skills_vector = vectorizer.transform([skills])
    return model.predict(skills_vector)[0]