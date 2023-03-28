import json

from django.shortcuts import render
import pandas as pd
import numpy as np
import nltk
from django.views.decorators.csrf import csrf_exempt

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from django.http import JsonResponse, HttpResponse

stop_words = set(stopwords.words('english'))
model = LinearSVC()
vectorizer = TfidfVectorizer()


def preprocess_text(text):
    # remove special characters
    text = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    text = text.encode('ascii', 'ignore').decode()
    # convert to lowercase
    text = text.lower()
    # tokenize text
    words = word_tokenize(text)
    # remove stopwords
    words = [w for w in words if not w in stop_words]
    return ' '.join(words)

def process():
    reviews = pd.read_csv("E:/pythonProject7/comment_service/abc.csv")
    #reviews = reviews.dropna()
    #reviews = reviews.dropna(axis=1)
    #reviews = reviews.fillna(0)
    #reviews.head()
    stop_words = set(stopwords.words('english'))
    reviews['review'] = reviews['review'].apply(preprocess_text)
    X = reviews['review'].values
    y = reviews['sentiment'].values
    X = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    #print(classification_report(y_test, y_pred))

@csrf_exempt
def analyze_review(request):
    process()
    review_text = request.POST.get("review")
    processed_text = preprocess_text(review_text)
    vectorized_text = vectorizer.transform([processed_text])
    sentiment = model.predict(vectorized_text)[0]
    resp = {}
    if sentiment:
        resp['sentiment'] = sentiment
    return HttpResponse(json.dumps(resp), content_type='application/json')

# if __name__ == '__main__':
#     print(analyze_review("The backpack looks good but the zippers keep getting stuck. Not worth the price."))
