"""
Category: Machine Learning
ID: Example 6
Description: Classifying handwritten digits using ```scikit-learn```
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

TODO:
"""


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.manifold import Isomap
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    digits = load_digits()
    print(digits.images.shape)

    # get the 2D representation of the images [n_samples, n_features]
    X = digits.data
    y = digits.target

    # reduce dimensionality
    iso = Isomap(n_components=2)
    iso.fit(digits.data)
    data_prj = iso.transform(digits.data)


    plt.scatter(data_prj[:, 0], data_prj[:, 1], c=digits.target,
                edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('Accent', 10))

    plt.colorbar(label='digit label', ticks=range(10))
    plt.clim(-0.5, 9.5)
    plt.show()

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

    # create the model
    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)
    accuracy_score(ytest, y_model)

    mat = confusion_matrix(ytest, y_model)
    sns.heatmap(mat, square=True, annot=True, cbar=False)
    plt.xlabel('predicted value')
    plt.ylabel('true value')
    plt.show()

    fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                            subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
        ax.text(0.05, 0.05, str(y_model[i]), transform=ax.transAxes, color='green' if (ytest[i] == y_model[i]) else 'red')
    plt.show()



if __name__ == '__main__':
    print("Running Example machine_learning/example_6")
    main()
    print("Done...")