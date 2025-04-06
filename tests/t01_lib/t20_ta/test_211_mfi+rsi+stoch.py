"""
@pyne
"""
from pynecore.lib import script, ta, close, high, low


@script.indicator(title="MFI+RSI+Stoch Test", shorttitle="mfi+rsi+stoch", overlay=False)
def main():
    return {
        "ta.mfi(close, 14)": ta.mfi(close, 14),
        "ta.rsi(close, 14)": ta.rsi(close, 14),
        "ta.stoch(close, high, low, 20)": ta.stoch(close, high, low, 20),
    }


def __test_mfi_rsi_stoch__(csv_reader, runner, dict_comparator, log):
    """ MFI / RSI / Stoch """
    with csv_reader('mfi+rsi+stoch.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 200:
                break
