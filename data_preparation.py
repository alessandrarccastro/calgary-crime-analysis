
# Importing necessary libraries
import pandas as pd



def remove_last_month(data):
    """
    Remove the last month of data from the dataset
    """
    #identify las year
    last_year = data['Year'].max()
    #identify last month
    last_month = data[data['Year'] == last_year]['Month'].max()
    #remove last month
    data = data[(data['Year'] != last_year) | (data['Month'] != last_month)]
    return data


# Time series data
# Date column

# Create a date column
def create_date_column(data):
    """
    Create a date column in the dataset
    """
    data['Date'] = (data['Year'].astype(str) + '-' + data['Month'].astype(str) + '-01') 
    data['Date'] = pd.to_datetime(data['Date'])
    return data


#time series object
def create_time_series(data, count_column):
    """
    Create a time series object
    """
    ts_data = data.groupby('Date')[count_column].sum()
    return ts_data

