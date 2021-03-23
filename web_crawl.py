import datetime
import pytz
import pandas as pd
import csv


# Record daily average over six months and update once per day
def six_months_data(file_path, url):
    web = pd.read_html(url)
    data = web[0].iloc[:, 0:6]
    data.columns = ['date', 'currency', 'offer(cash)', 'bid(cash)', 'offer(spot)', 'bid(spot)']
    data['currency'] = data['currency'].str.extract('\((\w+)\)')
    data.to_csv(file_path)
    return data


def daily_data_initial(file_path, url):
    web = pd.read_html(url)
    data = web[0].iloc[:, 0:5]
    data.columns = ['currency', 'offer(cash)', 'bid(cash)', 'offer(spot)', 'bid(spot)']
    data['currency'] = data['currency'].str.extract('\((\w+)\)')
    data = data[data.currency == 'AUD']
    data.reset_index()
    datetime_TW = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M')
    data.insert(0, 'Time', datetime_TW, True)
    data.reset_index(drop=True, inplace=True)
    data.to_csv(file_path, index=False)
    return data


# Update single day data to the existing csv
def daily_data_record(file_path, url, first_time):
    # Ensure the daily data would not be reset by an accident
    if first_time is True:
        data = daily_data_initial(file_path, url)
        return data

    web = pd.read_html(url)
    data = web[0].iloc[:, 0:5]
    data.columns = ['currency', 'offer(cash)', 'bid(cash)', 'offer(spot)', 'bid(spot)']
    data['currency'] = data['currency'].str.extract('\((\w+)\)')
    data = data[data.currency == 'AUD']
    datetime_TW = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M')
    data.insert(0, 'Time', datetime_TW, True)
    new_row = data.iloc[0, 0:6]
    # Append row to the data frame
    # Add contents of list as last row in the csv file
    with open(file_path, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv.writer(write_obj).writerow(new_row)

    return data


def initial_required():
    reply = input("Is this the First time using the system today ? (yes/no)")
    if reply.lower() == "yes":
        return True
    elif reply.lower() == "no":
        return False
    else:
        print("Unexpected reply")
        quit()




