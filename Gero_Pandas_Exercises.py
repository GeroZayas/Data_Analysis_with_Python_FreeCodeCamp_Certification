import pandas as pd
import numpy as np

X = ["A", "B", "C"]
print(X, type(X))

Y = pd.Series(X)
print(Y, type(Y))  # different type
