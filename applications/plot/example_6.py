"""
Category: Plotting
ID: Example6
Description: Pair plots with ```seaborn```
Taken From:

Details:


"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():

    filepath ='../../data/datasets/iris_data.csv'
    iris_set = pd.read_csv(filepath)

    print("Number or rows: ",iris_set.shape[0])
    print("Number or columns: ", iris_set.shape[1])
    print("Column names: ", iris_set.columns.tolist())

    sns.pairplot(iris_set, hue='species', height=3)
    plt.show()


if __name__ == '__main__':
    print("Running Example plotting/example_6")
    main()
    print("Done...")