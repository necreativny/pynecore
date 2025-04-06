"""
@pyne
"""
from pynecore.lib import script, ta, plot


@script.indicator(title="SAR", shorttitle="sar", overlay=True)
def main():
    plot(ta.sar(0.02, 0.02, 0.2), "ta.sar(0.02, 0.02, 0.2)", style=plot.style_cross, linewidth=2)


# noinspection PyShadowingNames
def __test_sar__(csv_reader, runner, dict_comparator):
    """ Parabolic SAR """
    with csv_reader('sar.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 200:
                break
