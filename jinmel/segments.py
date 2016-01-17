from datetime import date
from time import time


def dday(
    pl,
    year,
    month,
    day,
        fmt='D-{days}'):
    today = date.today()
    dest_day = date(year, month, day)
    delta = (dest_day - today)
    return [{
        'contents': fmt.format(days=delta.days),
        'highlight_groups': ['date']
    }]

def dday_percentage(
    pl,
    dest_year,
    dest_month,
    dest_day,
    src_year,
    src_month,
    src_day
):
    end_date = date(dest_year,dest_month,dest_day)
    start_date = date(src_year,src_month,src_day)
    total_days = (end_date - start_date).days
    today = date.fromtimestamp(time())
    current_days = (today - start_date).days
    dday = (end_date - today).days
    percentage = float(current_days) / float(total_days) * 100.0
    return [{
        'contents': "D-{0}({1:.1f}%)".format(dday,percentage),
        'highlight_groups': ['date']
    }]
