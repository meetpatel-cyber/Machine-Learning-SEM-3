# Create DataFrame using Pandas

import pandas as pd

x = {'Name':['Player_A','Player_B','Player_C'],
     'Age':[25,30,35],
     'Score':[1,2,3]}

df = pd.DataFrame(x)
print(df)