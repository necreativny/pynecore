"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="ALMA Test", shorttitle="ALMA_T", overlay=True)
def main():
    return {
        "ta.alma(close, 5, 0.85, 6)": ta.alma(close, 5, 0.85, 6),
        "ta.alma(close, 10, 0.55, 12)": ta.alma(close, 10, 0.55, 12),
    }


def __test_alma__(csv_reader, runner, dict_comparator, log):
    """ ALMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
