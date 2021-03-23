import datetime
import pytz
import time
import web_crawl as wc
import tool

# Constant
SIX_MONTHS_FILE = 'six_months(TWD->AUD).csv'
SIX_MONTHS_URL = 'https://rate.bot.com.tw/xrt/quote/l6m/AUD'
SINGLE_DAY_FILE = 'single_day(TWD->AUD).csv'
SINGLE_DAY_URL = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
UPDATE_TIME_INTERVAL = 60

# set time to terminate program
tz_TW = pytz.timezone('Asia/Taipei')
start_time = datetime.datetime.now(tz_TW).replace(hour=9, minute=0, second=0)
end_time = datetime.datetime.now(tz_TW).replace(hour=15, minute=30, second=0)


def main():
    wc.six_months_data(SIX_MONTHS_FILE, SIX_MONTHS_URL)
    first_time = wc.initial_required()
    current_time = datetime.datetime.now(tz_TW)
    # During trading hours, the currency data would be updated regularly
    while start_time <= current_time <= end_time:
        print(current_time.strftime('%Y-%m-%d %H:%M\n'))
        wc.daily_data_record(SINGLE_DAY_FILE, SINGLE_DAY_URL, first_time)
        first_time = False
        if tool.currency_change(SINGLE_DAY_FILE) is True:
            print("!!!")
        time.sleep(UPDATE_TIME_INTERVAL)
        current_time = datetime.datetime.now(tz_TW)


main()
