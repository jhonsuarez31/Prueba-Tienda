from datetime import datetime
import pytz


def datetimeNow(
    timezone="America/Bogota",
    to_str=False,
    to_format='%Y-%m-%d %H:%M:%S.%f'
):
    datetimeString = datetime.now(pytz.timezone(timezone)).strftime(to_format)
    if to_str:
        return datetimeString

    datetimeNew = datetime.strptime(datetimeString, to_format)

    return datetimeNew
