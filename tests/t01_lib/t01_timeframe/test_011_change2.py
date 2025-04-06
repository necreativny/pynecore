"""
@pyne
"""
from pynecore.lib import script, timeframe, plot


@script.indicator(title="Timeframe Change 2nd", shorttitle="tf_change2")
def main():
    plot(1 if timeframe.change("3D") else 0, "tf_change_3D")
    plot(2 if timeframe.change("7D") else 0, "tf_change_7D")
    plot(3 if timeframe.change("5W") else 0, "tf_change_5W")
    plot(4 if timeframe.change("7W") else 0, "tf_change_7W")
    plot(5 if timeframe.change("M") else 0, "tf_change_1M")
    plot(6 if timeframe.change("3M") else 0, "tf_change_3M")


def __test_timeframe_change_2__(csv_reader, runner, dict_comparator, log):
    """ timeframe.change() 2nd """
    from pathlib import Path
    syminfo_path = Path(__file__).parent / "data" / "timeframe.toml"
    exc_cout = 0
    with csv_reader('timeframe2.csv', subdir="data") as cr:
        for candle, _plot in runner(cr, dict(period="240"), syminfo_path=syminfo_path).run_iter():
            try:
                dict_comparator(_plot, candle.extra_fields)
            except AssertionError as e:
                exc_cout += 1
                log.error(f"Assertion error: {e}")
                if exc_cout > 0:
                    raise e
