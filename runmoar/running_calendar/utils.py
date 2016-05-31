from datetime import datetime, timedelta


def toDate(input_date):
    return datetime.strptime(input_date, '%Y-%m-%d')


def getDateRange(start_date, end_date):
    dates_to_check = []
    while start_date <= end_date:
        dates_to_check.append(start_date)
        start_date += timedelta(days=1)

    return dates_to_check
