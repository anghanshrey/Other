# python DATETIME & TIME MODULE

from datetime import datetime, timedelta , timezone
import time
import datetime

# Current Date and Time

def current_datetime():

    now = datetime.now()

    print("Current Date & Time : ", now)
    print("Year :" , now.year)
    print("Month :" , now.month)
    print("Day :" , now.day)
    print("Hour :" , now.hour)
    print("Mintue :" , now.minute)
    print("Second :" , now.second)

def time_seconds():

    seconds = time.time()

    print("Second since 1 Jan 1970 : ", seconds)

def format_datetime():

    now = datetime.now()

    print("DD-MM-YYYY : " , now.strftime("%d-%m-%y"))
    print("MM/DD/YYYY : " , now.strftime("%m/%d/%y"))
    print("12 - hours : " , now.strftime("%I : %M :%S %p"))
    print("24 - hours : " , now.strftime("%H:%M:%S"))

# Number of Days Between two Dates

def date_diffrence():
    """
    start_date = input("Enter start datr (YYYY-MM-DD) :")
    end_date = input("Enter end date(YYYY-MM-DD) :")

    date1 = datetime.strptime(start_date , "%Y-%m-%d")
    date2 = datetime.strptime(end_date , "%Y-%m-%d") 

    days = abs((date2 - date1).days)

    print("Total Days :" , days)
    """
    today = datetime.now()

    future_time = today - timedelta(days=15)

    print("Today : " , today.strftime("%d-%m-%Y"))
    print("Diff : " , future_time.strftime("%d-%m-%Y"))

#date_diffrence()

# UTC and Local time

def utc_local_time():
    utc_time = datetime.now(timezone.utc)
    local_time = datetime.now()

    print(utc_time)
    print(local_time)

#utc_local_time()

def custom_time():

    current_time = datetime.datetime(2025, 8, 21 , 12 , 30 , 40)
    print(current_time)

custom_time()
