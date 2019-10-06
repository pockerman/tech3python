"""
Category: Machine Learning
ID: Example 3
Description: Simple Classification with ```scikit-learn Guassian Naive Bayes```
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

Naive Bayes


Example applications/machine_learning/example_4.py  will use PCA to cast the
4-dimensional Iris data set into 2 dimensions. We will see that the species are quite
separated. This indicates to us that a relatively straightforward classification will most likely
be effective on the dataset.
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def main():

    iris = datasets.load_iris()

    print(iris.keys())
    print(iris['feature_names'])  # this should show 4 names thus data

    Xtrn, Xtst, ytrn, ytst = train_test_split(iris.data, iris.target, random_state=1, test_size=0.2)

    assert Xtrn.shape[0] == ytrn.shape[0], "Invalid shapes"

    # choose the model
    model = GaussianNB()

    #  fit model to data
    model.fit(Xtrn, ytrn)

    # predict on new data
    y_model = model.predict(Xtst)

    score = accuracy_score(ytst, y_model)

    print("Score for GaussinaNB: ", score)


if __name__ == '__main__':
    print("Running Example machine_learning/example_3")
    main()
    print("Done...")