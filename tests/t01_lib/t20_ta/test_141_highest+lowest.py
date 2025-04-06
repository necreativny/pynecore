"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="Highest+Lowest Test", shorttitle="highest+lowest", overlay=False)
def main():
    return {
        "ta.highest(10)": ta.highest(10),
        "ta.highest(close, 10)": ta.highest(close, 10),
        "ta.lowest(10)": ta.lowest(10),
        "ta.lowest(close, 10)": ta.lowest(close, 10),
        "ta.highestbars(10)": ta.highestbars(10),
        "ta.highestbars(close, 10)": ta.highestbars(close, 10),
        "ta.lowestbars(10)": ta.lowestbars(10),
        "ta.lowestbars(close, 10)": ta.lowestbars(close, 10),
    }


def __test_highest_lowest__(csv_reader, runner, dict_comparator, log):
    """ Highest + Lowest """
    with csv_reader('highest+lowest.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 200:
                break
