"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="CCI Test", shorttitle="CCI_T", overlay=False)
def main():
    return {
        # This also tests the dev() function
        "ta.cci(close, 20)": ta.cci(close, 20),
    }


def __test_cci__(csv_reader, runner, dict_comparator, log):
    """ CCI """
    with csv_reader('cci+cmo+cog.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
