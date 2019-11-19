"""
Category: Plotting
ID: Example4
Description: Load a data set with Pandas and plot a histogram plot
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
    ax = plt.axes()

    plt.hist(iris_set.sepal_length,  bins=15, alpha=0.5, histtype='bar', ec='black')
    plt.hist(iris_set.sepal_width, bins=15, alpha=0.5, histtype='bar', ec='black')


    plt.xlabel('Sepal Length (cm)/Sepal Width (cm)')
    plt.legend('Sepal Length vs Width')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()

if __name__ == '__main__':
    print("Running Example plotting/example_4")
    main()
    print("Done...")