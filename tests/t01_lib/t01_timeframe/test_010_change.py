"""
@pyne
"""
from pynecore.lib import script, timeframe, plot


@script.indicator(title="Timeframe Change", shorttitle="tf_change")
def main():
    plot(1 if timeframe.change("15") else 0, "tf_change_15")
    plot(1.5 if timeframe.change("240") else 0, "tf_change_240")
    plot(2 if timeframe.change("D") else 0, "tf_change_D")
    plot(2.2 if timeframe.change("2D") else 0, "tf_change_2D")
    plot(2.5 if timeframe.change("W") else 0, "tf_change_W")
    plot(2.8 if timeframe.change("3W") else 0, "tf_change_3W")
    plot(3 if timeframe.change("M") else 0, "tf_change_M")


def __test_timeframe_change1__(csv_reader, runner, dict_comparator, log):
    """ timeframe.change() """
    from pathlib import Path
    syminfo_path = Path(__file__).parent / "data" / "timeframe.toml"
    with csv_reader('timeframe.csv', subdir="data") as cr:
        for candle, _plot in runner(cr, syminfo_path=syminfo_path).run_iter():
            dict_comparator(_plot, candle.extra_fields)
