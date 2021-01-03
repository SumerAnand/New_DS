import pandas as pd
import numpy as np

df = pd.DataFrame ([[0.23, 'f1'], [5.36, 'f2']],
                   index=list ('pq'),
                   columns=list ('ab'))

df=df.rename(index={'p':'P'})
print(df)

new=list(np.random.randn(2))
df['c']=new
print(df)