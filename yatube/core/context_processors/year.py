import datetime as dt


def year(request):
    return {
        'year': int(dt.date.today().strftime('%Y'))
    }
