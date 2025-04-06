"""
@pyne
"""
from pynecore.lib import script, ta


@script.indicator(title="TR Test", shorttitle="tr")
def main():
    return {
        "ta.tr(false)": ta.tr(False),
        "ta.tr(true)": ta.tr(True),
        "ta.tr": ta.tr,
        "ta.atr(14)": ta.atr(14),
    }


def __test_tr__(csv_reader, runner, dict_comparator, log):
    """ TR / ATR """
    with csv_reader('tr.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
