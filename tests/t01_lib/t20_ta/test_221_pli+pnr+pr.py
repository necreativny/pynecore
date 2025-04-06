"""
@pyne
"""
from pynecore.lib import script, ta, close, color, plot


@script.indicator(title="PLI+PNR+PR Test", shorttitle="ppp", overlay=True)
def main():
    plot(ta.percentile_linear_interpolation(close, 20, 20),
         "ta.percentile_linear_interpolation(close, 20, 30)", color=color.orange)
    plot(ta.percentile_nearest_rank(close, 20, 20),
         "ta.percentile_nearest_rank(close, 20, 0)", color=color.olive, )
    plot(ta.percentrank(close, 33), "ta.percentrank(close, 33)", color=color.red)


# noinspection PyShadowingNames
def __test_ppp__(csv_reader, runner, dict_comparator, log):
    """ PLI+PNR+PR """
    with csv_reader('ppp.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 200:
                break
