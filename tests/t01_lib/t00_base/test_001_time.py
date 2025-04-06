"""
@pyne
"""
from pynecore.lib import (script, plot, display, syminfo, time, dayofmonth, dayofweek, timestamp,
                          hour, minute, month, second, weekofyear, year)


@script.indicator(title="Date/Time", shorttitle="datetime")
def main():
    plot(time, "time", display=display.data_window)
    plot(time + 5 * 60 * 1000, "time+", display=display.data_window)

    plot(dayofmonth, "dayofmonth")
    plot(dayofmonth(time + 5 * 60 * 1000), "dayofmonth_time")
    plot(dayofmonth(time + 10 * 60 * 1000, "Europe/Budapest"), "dayofmonth_time_tz")

    plot(dayofweek, "dayofweek")
    plot(dayofweek(time + 5 * 60 * 1000), "dayofweek_time")
    plot(dayofweek(time + 5 * 60 * 1000, "Europe/Budapest"), "dayofweek_time_tz")

    plot(hour, "hour")
    plot(hour(time + 5 * 60 * 1000), "hour_time")
    plot(hour(time + 5 * 60 * 1000, "Europe/Budapest"), "hour_time_tz")

    plot(minute, "minute")
    plot(minute(time + 5 * 60 * 1000), "minute_time")
    plot(minute(time + 5 * 60 * 1000, "Europe/Budapest"), "minute_time_tz")

    plot(month, "month")
    plot(month(time + 5 * 60 * 1000), "month_time")
    plot(month(time + 5 * 60 * 1000, "Europe/Budapest"), "month_time_tz")

    plot(second, "second")
    plot(second(time + 5 * 60 * 1000), "second_time")
    plot(second(time + 5 * 60 * 1000, "Europe/Budapest"), "second_time_tz")

    plot(weekofyear, "weekofyear")
    plot(weekofyear(time + 5 * 60 * 1000), "weekofyear_time")
    plot(weekofyear(time + 5 * 60 * 1000, "Europe/Budapest"), "weekofyear_time_tz")

    plot(year, "year")
    plot(year(time + 5 * 60 * 1000), "year_time")
    plot(year(time + 5 * 60 * 1000, "Europe/Budapest"), "year_time_tz")

    plot(timestamp(2016, 1, 19, 9, 30), "timestamp datetime 1")
    plot(timestamp(2019, 6, 19, 9, 30, 15), "timestamp datetime 2")
    plot(timestamp(syminfo.timezone, 2016, 1, 19, 9, 30), "timestamp datetime tz 1")
    plot(timestamp("GMT+6", 2016, 1, 19, 9, 30), "timestamp datetime tz 2")
    plot(timestamp("GMT+3", 2019, 6, 19, 9, 30, 15), "timestamp datetime tz 3")
    plot(timestamp(dateString="Feb 01 2020 22:10:05"), 'timestamp datestr 1')
    plot(timestamp("2011-10-10T14:48:00"), 'timestamp datestr 2')
    plot(timestamp("04 Dec 1995 00:12:00 GMT+5"), 'timestamp datestr 3')


def __test_time__(csv_reader, runner, dict_comparator, log):
    """ Date / Time """
    with csv_reader('time.csv', subdir="data") as cr:
        for i, (candle, _plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(_plot, candle.extra_fields)
            if i > 1152:
                break
