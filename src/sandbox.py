from random_data import data
import pandas as pd

# TEST create df
df = pd.DataFrame(data)
# find lowest and highest value of date_utc column_stack
print(df['date_utc'].min())
print(df['date_utc'].max())
print(df.dtypes)

# TEST write csv
df.to_csv('data.csv', sep=";", decimal=",", index=False)

# TEST filter
# start_date = pd.to_datetime("2024-11-17").tz_localize('UTC')
# end_date = pd.to_datetime("2028-11-20").tz_localize('UTC')
# print(start_date)
# print(end_date)
#
# df = pd.DataFrame(data)
# print(df.dtypes)
#
# dff = df.copy()
# dff['date_utc'] = pd.to_datetime(dff['date_utc'])
# print(dff.dtypes)
#
# dff = dff[(dff['date_utc'] >= start_date) & (dff['date_utc'] <= end_date)]
# print(dff.shape)