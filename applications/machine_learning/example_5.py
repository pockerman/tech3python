"""
Category: Machine Learning
ID: Example 5
Description: Clustering Iris data set with Gaussian Mixture Models
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

TODO: Fill in details about Gaussian Mixture Models
"""


from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    sns.set()

    iris = sns.load_dataset('iris')
    X_iris = iris.drop('species', axis=1)

    # choose the model...reduce the data set dimensionality to 2
    model = PCA(n_components=2)

    #  fit model to data
    model.fit(X_iris)

    Xiris_2d = model.transform(X_iris)
    iris['PCA1'] = Xiris_2d[:, 0]
    iris['PCA2'] = Xiris_2d[:, 1]

    model = GaussianMixture(n_components=3, covariance_type='full')

    #  fit model to data
    model.fit(X_iris)

    y_gmm = model.predict(X_iris)

    iris['cluster'] = y_gmm

    sns.lmplot('PCA1', 'PCA2', hue='species', col='cluster', data=iris, fit_reg=False)
    plt.show()


if __name__ == '__main__':
    print("Running Example machine_learning/example_5")
    main()
    print("Done...")