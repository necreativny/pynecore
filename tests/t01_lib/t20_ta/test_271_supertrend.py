"""
@pyne
"""
from pynecore.lib import script, ta, plot, na, color


@script.indicator(title="Supertrend", shorttitle="supertrend", overlay=True)
def main():
    supertrend, direction = ta.supertrend(3, 10)
    plot(supertrend if direction < 0 else na(float), "ta.supertrend(3, 10).up", color=color.green,
         style=plot.style_linebr)
    plot(supertrend if direction > 0 else na(float), "ta.supertrend(3, 10).down", color=color.red,
         style=plot.style_linebr)


# noinspection PyShadowingNames
def __test_sar__(csv_reader, runner, dict_comparator):
    """ Supertrend """
    with csv_reader('supertrend.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 200:
                break
