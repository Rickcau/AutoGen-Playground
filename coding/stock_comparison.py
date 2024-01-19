# filename: stock_comparison.py
import datetime
import pandas_datareader.data as web

# get the current date
today = datetime.date.today()

# fetch stock prices for META and TESLA for the current year
start_date = datetime.date(today.year, 1, 1)
end_date = today
meta_data = web.DataReader('META', 'yahoo', start_date, end_date)
tesla_data = web.DataReader('TSLA', 'yahoo', start_date, end_date)

# calculate year-to-date gain for META and TESLA
meta_ytd_gain = (meta_data['Close'][-1] - meta_data['Open'][0]) / meta_data['Open'][0] * 100
tesla_ytd_gain = (tesla_data['Close'][-1] - tesla_data['Open'][0]) / tesla_data['Open'][0] * 100

# compare year-to-date gain for META and TESLA
if meta_ytd_gain > tesla_ytd_gain:
    print("META has a higher year-to-date gain than TESLA.")
elif tesla_ytd_gain > meta_ytd_gain:
    print("TESLA has a higher year-to-date gain than META.")
else:
    print("META and TESLA have the same year-to-date gain.")