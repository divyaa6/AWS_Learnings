import pandas as pd
import numpy as np

df = pd.DataFrame({'A': np.arange(5), 'B': np.random.randn(5)})
df['C'] = df['A'] * df['B']
df.to_csv('output.csv', index=False)
print("ETL job completed successfully!")
