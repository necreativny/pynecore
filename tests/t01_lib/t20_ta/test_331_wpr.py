"""
@pyne
"""
from pynecore.lib import script, ta, plot


@script.indicator(title="WPR Test", shorttitle="wpr", overlay=True)
def main():
    plot(ta.wpr(20), "ta.wpr(20)")


# noinspection PyShadowingNames
def __test_wpr__(csv_reader, runner, dict_comparator, log):
    """ WPR """
    with csv_reader('wpr.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
