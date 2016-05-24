from datetime import datetime


def toDate(input_date):
    return datetime.strptime(input_date, '%Y-%m-%d')
