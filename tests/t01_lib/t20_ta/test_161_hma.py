"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="HMA Test", shorttitle="HMA_T", overlay=True)
def main():
    return {
        "ta.hma(close, 9)": ta.hma(close, 9),
        "ta.hma(close, 20)": ta.hma(close, 20),
    }


def __test_hma__(csv_reader, runner, dict_comparator, log):
    """ HMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
