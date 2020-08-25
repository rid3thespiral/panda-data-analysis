import pandas as pd

#different constructors for Datetime and Datetimeindex
#timestamp()
print(pd.Timestamp("30/06/1993"))
print(pd.Timestamp("30-06-1993"))
print(pd.Timestamp("30-06/1993"))
print(pd.Timestamp("30 Jun, 1993"))
print(pd.Timestamp(436380629, unit="ns"))
print(pd.Timestamp(436380629.5, unit="s"))
print(pd.Timestamp(2020, 5, 9, 18, 44, 43))

#to_datetime()
print(pd.to_datetime("30/06/1993"))
#passing a list
print(pd.to_datetime(["30/06/1993", "20/06/1993"])) #return DatetimeIndex
#passing a Series object
serie=pd.Series(["1981", "30-06/1993", "30-06/1994", "30-06/1993 08:45"])
print(pd.to_datetime(serie))

#daterange()
print(pd.date_range(start="2019/01/01", end="31/12/2019")) #collection of Timestamps, Datatimeindex, len 365
print(pd.date_range(start="2019/01/01", end="31/12/2019", freq="M")) #collection of Timestamps, Datetimeindex, len 12
print(pd.date_range(start="2019/01/01", end="31/12/2019", freq="B")) #business day
print(pd.date_range(start="2019/01/01", end="31/12/2019", freq="12H")) #by hours
print(pd.date_range(start="2019/01/01", end="31/12/2019", freq="Q")) #by quarter
print(pd.date_range(start="2019/01/01", periods=56)) #by 56, default days
print(pd.date_range(start="2019/01/01", periods=56, freq="W-SUN")) #by 56, default week from sunday
print(pd.date_range(end="2019/01/01", periods=56, freq="W")) #backwards

#objects Period and PeriodIndex as collection of Periods
start=pd.Period("2020-01-01")
end=pd.Period("2020-02-01")
print(start.start_time, start.end_time)
#period_range()
print(pd.period_range(start, end, freq="M").to_timestamp())
print(pd.date_range("2020-01-01", "2020-02-01", freq="M").to_period())

#Timedelta and Timedeltaindex: diff absolute time
time1=pd.Timestamp("2020-01-11 12:00:00")
time2=pd.Timestamp("2020-03-11 12:00:00")
print(time2-time1, type(time2-time1)) #timedelta object


