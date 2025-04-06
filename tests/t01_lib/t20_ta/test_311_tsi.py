"""
@pyne
"""
from pynecore.lib import script, ta, close, plot


@script.indicator(title="TSI Test", shorttitle="tsi", overlay=True)
def main():
    plot(ta.tsi(close, 12, 26), "ta.tsi(close, 12, 26)")


# noinspection PyShadowingNames
def __test_tsi__(csv_reader, runner, dict_comparator, log):
    """ TSI """
    with csv_reader('tsi.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
