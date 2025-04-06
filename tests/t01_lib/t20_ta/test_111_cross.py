"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="Cross Test", shorttitle="cross_T", overlay=False)
def main():
    ema1 = ta.ema(close, 5)
    ema2 = ta.ema(close, 11)

    return {
        "ta.cross(ema1, ema2)": 0.5 if ta.cross(ema1, ema2) else 0.0,
        "ta.crossover(ema1, ema2)": 1.0 if ta.crossover(ema1, ema2) else 0.0,
        "ta.crossunder(ema1, ema2)": -1.0 if ta.crossunder(ema1, ema2) else 0.0,
    }


def __test_cross__(csv_reader, runner, dict_comparator, log):
    """ Cross """
    with csv_reader('cross.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 150:
                break
