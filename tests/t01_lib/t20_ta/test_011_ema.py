"""
@pyne
"""
from pynecore.lib import script, ta, close, ohlc4


@script.indicator(title="EMA Test", shorttitle="EMA_T", overlay=True)
def main():
    return {
        "ta.ema(close, 20)": ta.ema(close, 20),
        "ta.ema(ohlc4, 10)": ta.ema(ohlc4, 10),
    }


def __test_ema__(csv_reader, runner, dict_comparator, log):
    """ EMA """

    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
