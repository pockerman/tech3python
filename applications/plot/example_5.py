"""
Category: Plotting
ID: Example5
Description: Two scatter plots within a figure
Taken From:

Details:


"""

import matplotlib.pyplot as plt
import pandas as pd

def main():

    filepath ='../../data/datasets/iris_data.csv'
    iris_set = pd.read_csv(filepath)

    print("Number or rows: ",iris_set.shape[0])
    print("Number or columns: ", iris_set.shape[1])
    print("Column names: ", iris_set.columns.tolist())

    # A simple scatter plot with Matplotlib
    plt.plot(iris_set.sepal_length, iris_set.sepal_width, ls='', marker='o', label='Sepal')
    plt.plot(iris_set.petal_length, iris_set.petal_width, ls='', marker='o', label='Petal')

    plt.xlabel('Sepal Length (cm)/Petal Length (cm) ')
    plt.ylabel('Sepal Width (cm)/Petal Width (cm)')
    plt.legend()
    plt.title('Sepal Length vs Width')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()


if __name__ == '__main__':
    print("Running Example plotting/example_5")
    main()
    print("Done...")