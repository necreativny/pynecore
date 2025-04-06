"""
@pyne
"""
from pynecore.lib import script, ta, close, hl2, plot


@script.indicator(title="RCI", shorttitle="rci", overlay=True)
def main():
    plot(ta.rci(close, 5), "ta.rci(close, 5)")
    plot(ta.rci(close, 20), "ta.rci(close, 20)")
    plot(ta.rci(hl2, 20), "ta.rci(hl2, 20)")


# noinspection PyShadowingNames
def __test_rci__(csv_reader, runner, dict_comparator):
    """ RCI """
    with csv_reader('rci.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 200:
                break
