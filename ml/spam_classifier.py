import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier


def spam_detector(train_df, valid_df, test_df):
    vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2))

    train_df_vector = vectorizer.fit_transform(train_df["text"]).toarray()
    valid_df_vector = vectorizer.transform(valid_df["text"]).toarray()
    test_df_vector = vectorizer.transform(test_df["text"]).toarray()

    models = {
        "LogisticRegression": LogisticRegression(random_state=0),
        "MultinomialNB": MultinomialNB(),
        "DecisionTreeClassifier": DecisionTreeClassifier(random_state=0),
        "LinearSVC": LinearSVC(),
    }

    result = {}
    best_model = {}
    
    for model_name, model in models.items():
        model.fit(train_df_vector, train_df["label"].values)
        valid_predictions = model.predict(valid_df_vector)
        result[model_name] = confusion_matrix(valid_df["label"], valid_predictions)
        best_model[model_name] = accuracy_score(valid_df["label"], valid_predictions, normalize=False)
 

    best_classifier = max(best_model, key=best_model.get)
    prediction = models[best_classifier].predict(test_df_vector)

    output = {'result': result, 'best_classifier': best_classifier, 'test_df_vector': test_df_vector, 'prediction':prediction}
    return output


if __name__ == "__main__":
    train_df = pd.read_csv("./naver/data/train.csv")
    valid_df = pd.read_csv("./naver/data/valid.csv")
    test_df = pd.read_csv("./naver/data/test.csv")

    train_df["label"] = train_df["label"].map({"ham": 1, "spam": 0})
    valid_df["label"] = valid_df["label"].map({"ham": 1, "spam": 0})
    test_df["label"] = test_df["label"].map({"ham": 1, "spam": 0})

    result = spam_detector(train_df, valid_df, test_df)
