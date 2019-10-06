"""
Category: Machine Learning
ID: Example 4
Description: Reduce dimensionality of Iris data set
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

The Iris data set is 4 dimensional. Concretely:

'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'

we want to reduce the dimensions of the data set in order to be able to visualize it.
Dimensionality reduction attempts to lower the dimension of a data set while simultaneously
retaining the essential features.

Principal Component Analysis or PCA is a dimensionality reduction technique.

"""



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

    sns.lmplot('PCA1', 'PCA2', hue='species', data=iris, fit_reg=False)
    plt.show()

if __name__ == '__main__':
    print("Running Example machine_learning/example_4")
    main()
    print("Done...")