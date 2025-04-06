"""
@pyne
"""
from pynecore.lib import script, ta, hlcc4, high


@script.indicator(title="RMA Test", shorttitle="RMA_T")
def main():
    return {
        "ta.rma(hlcc4, 5)": ta.rma(hlcc4, 5),
        "ta.rma(high, 15)": ta.rma(high, 15),
    }


def __test_rma__(csv_reader, runner, dict_comparator, log):
    """ RMA """
    with csv_reader('ma.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
