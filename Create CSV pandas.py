# A CSV file can be created using Pandas by creating a DataFrame and saving it using to_csv().

import pandas as pd

data = {
    'Name': ['AAA', 'BBB', 'CCC'],
    'Age': [20, 21, 22],
    'City': ['NYC', 'IL', 'LA']
}
df = pd.DataFrame(data)
df.to_csv('my_data.csv', index=False)
print("CSV created")