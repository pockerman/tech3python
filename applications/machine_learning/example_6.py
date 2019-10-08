"""
Category: Machine Learning
ID: Example 6
Description: Classifying handwritten digits using ```scikit-learn```
Taken From: Code from the book Python Data Science Handbook
https://jakevdp.github.io/PythonDataScienceHandbook/

Details:

TODO:
"""


from sklearn.mixture import GaussianMixture
from sklearn.manifold import Isomap
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    digits = load_digits()
    print(digits.images.shape)


    # let's plot the images

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


if __name__ == '__main__':
    print("Running Example machine_learning/example_6")
    main()
    print("Done...")