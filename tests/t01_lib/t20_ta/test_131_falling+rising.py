"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="Falling+Rising Test", shorttitle="falling+rising", overlay=False)
def main():
    ema = ta.ema(close, 20)

    falling = ta.falling(ema, 5)
    rising = ta.rising(ema, 5)

    return {
        "ta.falling(ema, 5)": -1.0 if falling else 0.0,
        "ta.rising(ema, 5)": 1.0 if rising else 0.0,
    }


def __test_falling_rising__(csv_reader, runner, dict_comparator, log):
    """ Falling + Rising """
    with csv_reader('falling+rising.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 200:
                break
