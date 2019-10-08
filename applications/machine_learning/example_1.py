"""
Category: Machine Learning
ID: Example 1
Description: K-Nearest Neighbors with scikit-learn
Taken From:

Details:


"""

from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier


def main():

    X, y = make_classification(n_samples=1000, n_features=20)
    model = KNeighborsClassifier()
    model.fit(X, y=y)
    score = model.score(X, y)
    print("Score is {0} ".format(score))


if __name__ == '__main__':
    print("Running Example machine_learning/example_1")
    main()
    print("Done...")