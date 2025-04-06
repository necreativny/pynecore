"""
@pyne
"""
from pynecore.lib import script, ta, close, plot


@script.indicator(title="Valuewhen Test", shorttitle="valuewhen", overlay=True)
def main():
    slow = ta.sma(close, 7)
    fast = ta.sma(close, 14)
    plot(ta.valuewhen(ta.cross(slow, fast), close, 1), "ta.valuewhen(ta.cross(slow, fast), close, 1)")


# noinspection PyShadowingNames
def __test_valuewhen__(csv_reader, runner, dict_comparator, log):
    """ Valuewhen """
    with csv_reader('valuewhen.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
