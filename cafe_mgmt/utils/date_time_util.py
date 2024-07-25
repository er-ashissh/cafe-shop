from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import operator, pytz


class DateTimeUtil:

    
    '''
    Get Current Date
    @request: None
    @response: string date_time | Ex: '2020-08-30'
    '''
    def get_current_date():
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d")
        return date_time
    
    
    '''
    Get Current Date & Time
    @request: None
    @response: string date_time | Ex: '2020-08-30 12:07:42'
    '''
    def get_current_datetime():
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return date_time


    '''
    Get Current UTC + Country UTC Time 
    @request: int country_id
    @response: string date_time | Ex: '2020-04-26 11:08:28'
    '''
    def get_current(country_id):
        utc = Country.objects.get(id=country_id).utc
        return ( (operator.add if utc[0]=='+' else operator.sub) (datetime.utcnow(), (timedelta(hours=int(utc[1])) + timedelta(minutes=int(utc[2]))))).strftime('%Y-%m-%d %H:%M:%S')


    '''
    Get Current TimeStamp
    @request: None
    @response: int timestamp | Ex: 1589699311
    '''
    def get_current_timestamp():
        return int(datetime.timestamp(datetime.now()))


    '''
    Get DateTime TimeStamp
    @request: date_time str 2020-07-08 00:00:00
    @response: int timestamp | Ex: 1594166400
    '''
    def get_datetime_timestamp(date_time):
        return int(datetime.timestamp(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')))


    '''
    Get Current TimeStamp
    @request: None
    @response: int timestamp | Ex: 20200810071212
    '''
    def get_datetime_int():
        return int((datetime.now()).strftime('%Y%m%d%H%M%S'))


    '''
    Remove Time from DateTime
    @request: str date_time | Ex: '2020-04-26 11:08:28'
    @response: string date | Ex: '2020-04-26'
    '''
    def remove_time_from_datetime(date_time):
        return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').date()


    '''
    Add Days in Date
    @request: string date | Ex: '2020-04-26' &  int add_day | Ex: 2 
    @response: string date | Ex: '2020-04-28'
    '''
    def add_day_in_date(date, add_day):
        days_add_in_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=add_day)
        return DateTimeUtil.remove_time_from_datetime(str(days_add_in_date))


    '''
    Add Days in DateTime
    @request: string date_time | Ex: '2020-06-10 12:07:42' &  int add_day | Ex: 3
    @response: string date_time | Ex: '2020-06-13 12:07:42'
    '''
    def add_day_in_datetime(date_time:str, add_days:int) -> str:
        convert_to_date_obj =  datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        add_days_in_date_time = convert_to_date_obj + relativedelta(days=add_days)
        return add_days_in_date_time.strftime('%Y-%m-%d %H:%M:%S')


    '''
    Subtract Days in Date
    @request: string date | Ex: '2020-04-26' &  int add_day | Ex: 2 
    @response: string date | Ex: '2020-04-28'
    '''
    def subtract_day_in_date(date, subtract_day):
        days_subtract_in_date = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=subtract_day)
        return DateTimeUtil.remove_time_from_datetime(str(days_subtract_in_date))


    '''
    Get Human Readable Date Time format
    @request: datetime date_time | Ex: '2020-08-01T15:14:52.770971'
    @response: string date_time | Ex: '2020-08-01 15:14:52'
    '''
    def format_date_time(date_time):
        return str(date_time)[:10] + ' ' + str(date_time)[11:19]


    '''
    Remove hyphen, colan, space from DateTime 
    @request: string date_time | Ex: '2020-06-10 12:07:42'
    @response: int date_time | Ex: '20200613120742'
    '''
    def rm_hyphen_from_datetime(date_time:str) -> str:
        clean_dt = int(date_time.replace("-","").replace(":","").replace(" ",""))
        return clean_dt