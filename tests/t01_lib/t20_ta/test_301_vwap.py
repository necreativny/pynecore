"""
@pyne
"""
from pynecore.lib import script, ta, close, color, plot, timeframe


@script.indicator(title="VWAP Test", shorttitle="vwma", overlay=True)
def main():
    plot(ta.vwap(close), "ta.vwap(close)", color.white, 3)
    plot(ta.vwap(close, timeframe.change("240")), "ta.vwap(close, timeframe.change(\"240\"))", color.yellow, 2)

    vwap, upper_band, lower_band = ta.vwap(close, timeframe.change("360"), 2.0)
    plot(vwap, "ta.vwap(close, timeframe.change(\"360\"), 2.0).vwap", color.aqua, linewidth=2)
    plot(upper_band, "ta.vwap(close, timeframe.change(\"360\"), 2.0).upper_band", color.blue, linewidth=1)
    plot(lower_band, "ta.vwap(close, timeframe.change(\"360\"), 2.0).lower_band", color.blue, linewidth=1)


# noinspection PyShadowingNames
def __test_vwap__(csv_reader, runner, dict_comparator, log):
    """ VWAP """
    from pathlib import Path
    syminfo_path = Path(__file__).parent / "data" / "vwap.toml"
    with csv_reader('vwap.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr, syminfo_path=syminfo_path).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 300:
                break
