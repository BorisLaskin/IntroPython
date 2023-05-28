import pandas as pd
path = r"E:\CODE\Python\Знакомство с Python\Lections\lect5\1.csv"
print(path)
df = pd.read_csv(path)

import matplotlib.pyplot as mpl
mpl.polar(df)
