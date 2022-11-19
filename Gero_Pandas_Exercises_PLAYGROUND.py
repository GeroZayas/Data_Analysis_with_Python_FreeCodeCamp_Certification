import pandas as pd

data = {"name": ["Sally", "Mary", "John", "Mary"], "age": [50, 40, 30, 40]}

df = pd.DataFrame(data)

s = df.duplicated()

print(s)
