import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils.class_weight import compute_class_weight
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

class Logistic_Gender:
    def __init__(self, lambda_c = 5):
        self.name = 'Logistic Regression'
        self.model = LogisticRegression()
        self.vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))
        self.C = lambda_c
    def train(self, train_X, train_y, valid_X, valid_y):
        X_train_vec = self.vectorizer.fit_transform(train_X)
        X_test_vec = self.vectorizer.transform(valid_X)
        class_weights = compute_class_weight('balanced', classes=[0, 1], y=train_y)
        model = LogisticRegression(
            penalty='l2', 
            C=self.C, 
            class_weight={0: class_weights[0], 1: class_weights[1]}
        )
        model.fit(X_train_vec, train_y)
        cv_scores = cross_val_score(model, X_train_vec, train_y, cv=5, scoring='accuracy')
        mean_cv_score = cv_scores.mean()
        std_cv_score = cv_scores.std()
        self.model = model
        return cv_scores, mean_cv_score, std_cv_score
    def predict(self, test_X, test_y = None):
        X_test_vec = self.vectorizer.transform(test_X)
        pred = self.model.predict(X_test_vec)
        return pred
    def metric(self, test_X, test_y):
        pred = self.predict(test_X, test_y)
        accuracy = accuracy_score(test_y, pred)
        recall = recall_score(test_y, pred)
        precision = precision_score(test_y, pred)
        f1 = f1_score(test_y, pred)
        return accuracy, recall, precision, f1