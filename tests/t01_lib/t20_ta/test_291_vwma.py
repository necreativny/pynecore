"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="VWMA Test", shorttitle="vwma", overlay=True)
def main():
    return {
        "ta.vwma(close, 20)": ta.vwma(close, 20),
    }


def __test_vwma__(csv_reader, runner, dict_comparator, log):
    """ VWMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
