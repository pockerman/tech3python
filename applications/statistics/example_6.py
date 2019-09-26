"""
Category: Statistics
ID: Example 6
Description: Using Pandas
Taken From: https://realpython.com/linear-regression-in-python/
Dependencies NumPy, scikit-learn, Pandas
"""

import pandas as pd

def main():
    data = {
        'Name': pd.Series(['Alex', 'George', 'Jane', 'John', 'Catherine', 'Nick',
                           'Edward', 'Jason', 'Gerard', 'Nocola', 'Richard', 'Yonas']),
        'Age': pd.Series([34, 26, 25, 27, 30, 54, 23, 43, 40, 30, 28, 46]),
        'Height': pd.Series([114.23, 173.24, 153.98, 172.0, 153.20, 164.6,
                             183.8, 163.78, 172.0, 164.8])
    }
    df = pd.DataFrame(data)

    print(df.std())  #

if __name__ == '__name__':

    print("Running Example statistics/example_6")
    main()
    print("Done...")