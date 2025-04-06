"""
@pyne
"""
from pynecore.lib import script, ta, hlc3


@script.indicator(title="SWMA Test", shorttitle="swma", overlay=True)
def main():
    return {
        "ta.swma(hlc3)": ta.swma(hlc3),
    }


def __test_swma__(csv_reader, runner, dict_comparator, log):
    """ SWMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
