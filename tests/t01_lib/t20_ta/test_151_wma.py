"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="WMA Test", shorttitle="WMA_T", overlay=True)
def main():
    return {
        "ta.wma(close, 5)": ta.wma(close, 5),
        "ta.wma(close, 20)": ta.wma(close, 20),
    }


def __test_wma__(csv_reader, runner, dict_comparator, log):
    """ WMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
