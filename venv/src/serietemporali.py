import pandas as pd
from pathlib import Path
import datetime

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

#Constructor Timedelta()
td1=pd.Timedelta(days = 1, minutes=50) #months not allowed

#Constructor to_timedelta(): accepting list or Series
td1index=pd.to_timedelta(['1 days 01:10:22', '45s', '1 W 2 days']) #obtaining timedeltaindex as collection of timedelta objects
print(td1index)

#Constructor timedelta_range() to create timedeltaindexes
print(pd.timedelta_range(start='1 W', periods=5))
print(pd.timedelta_range(start='1 W', periods=5, closed='left'))
print(pd.timedelta_range(start='1 W', periods=5, closed='right'))
print(pd.timedelta_range(start='1 W', end='2 days', freq="D"))

#.dt time-attributes
s = pd.Series(pd.date_range(start="2020/01/01",end="2020/12/31"))
df = s.to_frame(name="2020")
print(df)
df["giorno"]=df["2020"].dt.day_name()
print(df)
print(df["2020"].dt.month)

#Timestamps method and attributes
df = pd.Series(data = "random values", index= pd.date_range(start="2020/01/01", end="2020/12/31")).to_frame("2020")
giorno=df.index[0] #timestamp
print(giorno.day)
print(giorno.is_month_start)
print(giorno.is_month_end)
print(giorno.day_name())
print(giorno.month_name())

#datetimeindex method and attributes
print(df.index.day_name())
df.insert(0, column="dayname", value= df.index.day_name())
print(df)
print(df[df["dayname"] == "Friday"]) #only fridays

#read time series from external files
pathfile = str(Path(__file__).parents[2])+"/materials/FB.csv"#fb stock prices, without weekends
pathfile2 = str(Path(__file__).parents[2])+"/materials/FB2.csv" #opening-market hour
df = pd.read_csv(pathfile)
print(df.info()) #date dtype object
df.set_index("Date", inplace=True)
df.index=pd.to_datetime(df.index)

#same conversion from read_csv method
df = pd.read_csv(pathfile, parse_dates=["Date"], index_col="Date")
print(df.info)

df2 = pd.read_csv(pathfile2,
                  parse_dates=["Date"],
                  date_parser= lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %I_%p'))
#formatting and converting strings to dates with python stdlib
print(df2.info())

#loc[] and iloc[] with Datetimeindex objects
print(df.index)
print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[-3:-1])
print(df.iloc[[0,1-1]])
print(df.head())
print(df.loc['2019-05-17'])
print(df.loc['2019-05-17': '2019-05-21'])
print(df.loc['2019-05']) #may
print(df.loc['2020-01-01':])

#reindex(): fill weekends with business data
fb = pd.read_csv(pathfile, parse_dates=["Date"], index_col="Date").round(2)
print(fb)
print(fb.index.min()) #start_date
print(fb.index.max()) #end_date
indexnew= pd.date_range(start=fb.index.min(), end=fb.index.max(), freq="D")
fb= fb.reindex(indexnew, method="ffill")

#resample(): resampling time series
months=fb.resample("MS")
print(months.groups)
months.get_group('2019-08-01 00:00:00')
print(months.first())
print(months.last())
print(months.mean())
print(fb.resample("M", kind="period").mean())
print(fb.resample("W", kind="period").agg({"Open": "min", "Close": "max"}))

