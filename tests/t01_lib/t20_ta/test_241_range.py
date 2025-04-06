"""
@pyne
"""
from pynecore.lib import script, ta, close, plot


@script.indicator(title="Range", shorttitle="range", overlay=True)
def main():
    plot(ta.range(close, 20), "ta.range(close, 20)")


# noinspection PyShadowingNames
def __test_range__(csv_reader, runner, dict_comparator, log):
    """ Range """
    with csv_reader('range.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
