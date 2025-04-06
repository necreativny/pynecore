"""
@pyne
"""
from pynecore.lib import script, ta, close, color, plot


@script.indicator(title="Pivot Test", shorttitle="pivot", overlay=True)
def main():
    # NOTE: these tests also tests the highest and lowest functions
    plot(ta.pivothigh(10, 5), "ta.pivothigh(10, 5)")
    plot(ta.pivothigh(close, 10, 5), "ta.pivothigh(close, 10, 5)", color=color.green)
    plot(ta.pivotlow(10, 5), "ta.pivotlow(10, 5)")
    plot(ta.pivotlow(close, 10, 5), "ta.pivotlow(close, 10, 5)", color=color.green)


# noinspection PyShadowingNames
def __test_pivot__(csv_reader, runner, dict_comparator, log):
    """ Pivot """
    with csv_reader('pivot.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 300:
                break
