"""
@pyne
"""
from pynecore import Series
from pynecore.lib import script, ta, close, bar_index, plot, na


@script.indicator(title="Series If For", shorttitle="SerIfFor")
def main():
    ema1: Series[float] = na(float)
    ema2: Series[float] = na(float)

    for i in range(1, 4):
        # 1st (i=0) add new value, after (i>0) set, no add
        ema1 = ta.ema(close * i, 5)

    if bar_index % 4 == 3:
        # The gaps should be na
        ema2 = ta.ema(close, 10)

    plot(ema1, "ema1")
    plot(ema1[1], "ema1[1]")
    plot(ema2, "ema2")
    plot(ema2[2], "ema2[2]")


def __test_series_if__(csv_reader, runner, dict_comparator, log):
    """ Series If+For """
    with csv_reader('series_if_for.csv', subdir="data") as cr:
        for i, (candle, _plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(_plot, candle.extra_fields)
            if i > 100:
                break
