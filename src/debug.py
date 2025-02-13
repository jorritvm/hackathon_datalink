from numpy.ma.extras import column_stack

from random_data import data
import pandas as pd

df = pd.DataFrame(data)
# find lowest and highest value of date_utc column_stack
print(df['date_utc'].min())
print(df['date_utc'].max())