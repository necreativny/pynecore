"""
@pyne
"""
from pynecore.lib import script, ta, close, color, plot


@script.indicator(title="LinReg Test", shorttitle="LinReg_T", overlay=True)
def main():
    plot(ta.linreg(close, 20, 0), "ta.linreg(close, 20, 0)", color=color.orange, linewidth=2)
    plot(ta.linreg(close, 20, 10), "ta.linreg(close, 20, 10)", color=color.blue, linewidth=2)


# noinspection PyShadowingNames
def __test_linreg__(csv_reader, runner, dict_comparator, log):
    """ Linear regression """
    with csv_reader('linreg.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 200:
                break
