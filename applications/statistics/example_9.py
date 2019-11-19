"""
Category: Statistics
ID: Example 9
Description: Examine Iris dataset
Taken From:
Dependencies:
"""


import matplotlib.pyplot as plt
import pandas as pd

def main():

    filepath ='../../data/datasets/iris_data.csv'
    iris_set = pd.read_csv(filepath)

    print("Number or rows: ",iris_set.shape[0])
    print("Number or columns: ", iris_set.shape[1])
    print("Column names: ", iris_set.columns.tolist())

    print("Unique species: ", set(iris_set['species']))

    print("\n")

    # remove Iris- string
    iris_set['species'] = iris_set.species.str.replace('Iris-', '')
    species = iris_set['species']

    # let's count the occurence of each species
    print("virginica species: ", species.value_counts()['virginica'])
    print("setosa species: ", species.value_counts()['setosa'])
    print("versicolor species: ", species.value_counts()['versicolor'])

    print("\n")
    # get a description of the statistics
    print(iris_set.describe())

if __name__ == '__main__':
    print("Running Example plotting/example_9")
    main()
    print("Done...")