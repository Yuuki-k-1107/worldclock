from datetime import datetime
import pytz


def get_local_time(tz):
    # candidates of tz(partly)
    # Asia/Tokyo
    # Europe/London
    # America/New_York
    #
    # set timezone
    local_tz = pytz.timezone(tz)
    # datetime.utcnow() provides the current time of UTC
    # localize the UTC time with .astimezone(local_tz)
    #local_now = datetime.utcnow().astimezone(local_tz)
    local_now = datetime.now(local_tz)
    # %H:Hour, %M:Minute
    #return local_now.strftime("%H"), local_now.strftime("%M")
    return local_now


def get_minute(localized_time):
    return localized_time.strftime("%H")


def get_second(localized_time):
    return localized_time.strftime("%M")


def get_time_text(tz):
    return "{}:{}".format(get_minute(get_local_time(tz)), get_second(get_local_time(tz)))

