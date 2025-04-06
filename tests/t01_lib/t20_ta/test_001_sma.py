"""
@pyne
"""
from pynecore.lib import script, close, hl2, hlc3, ta


@script.indicator(title="SMA Test", shorttitle="SMA_T", overlay=True)
def main():
    return {
        "ta.sma(close, 10)": ta.sma(close, 10),
        "ta.sma(hl2, 20)": ta.sma(hl2, 20),
        "ta.sma(hlc3, 15)": ta.sma(hlc3, 15)
    }


def __test_sma__(csv_reader, runner, dict_comparator, log):
    """ SMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
