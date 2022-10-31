import pandas as pd
import numpy as np

# X = ["A", "B", "C"]
# print(X, type(X))

# Y = pd.Series(X)
# print(Y, type(Y))  # different type

# Y.name = "My letters"

# print(Y)

# print(Y.values)

names_series = pd.Series(["Elisa", "Gero", "Mar", "Enrique", "Cristina"])

print(names_series)

# CREATE INDEXES:
indexes = ["Mother", "The programmer", "Girlfriend", "Father", "Stepmother"]

# PUT INDEXES TO SERIES:
names_series.index = indexes

# print(
#     f"""
# {names_series}

# """
# )

# SHOW THE FIRST ELEMENT:

print(names_series[0])  # Elisa
print(names_series.iloc[0])  # Elisa
print(names_series["Mother"])  # Elisa

# SHOW THE LAST ELEMENT:

print(names_series[-1])  # Cristina
print(names_series.iloc[-1])  # Cristina
print(names_series["Stepmother"])  # Cristina


# Separator ------------------------------
print("-" * 20)

# SHOW ALL MIDDLE ELEMENTS:

print(names_series[1:-1])


# Separator ------------------------------
print("-" * 20)

# SHOW ELEMENTS IN REVERSE POSITION:

# print(names_series[::-1])


# Separator ------------------------------
print("-" * 20)

names_series = names_series[::-1]
print(names_series)


# Separator ------------------------------
print("-" * 20)

names_series += " [Great Person]"
print(names_series)


# Separator ------------------------------
print("-" * 20)
