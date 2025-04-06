"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="Min+Max+Median+Mode Test", shorttitle="mmmm", overlay=False)
def main():
    return {
        "min(close)": ta.min(close),
        "max(close)": ta.max(close),
        "median(close)": ta.median(close, 20),
        "mode(close)": ta.mode(close, 20),
    }


# noinspection PyShadowingNames
def __test_min_max_median_mode__(csv_reader, runner, dict_comparator, log):
    """ min, max, median, mode """
    with csv_reader('min+max+median+mode.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 200:
                break
