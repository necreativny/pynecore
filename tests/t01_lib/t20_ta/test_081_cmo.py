"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="CMO Test", shorttitle="CMO_T", overlay=False)
def main():
    return {
        # This also tests the dev() function
        "ta.cmo(close, 20)": ta.cmo(close, 20),
    }


def __test_cmo__(csv_reader, runner, dict_comparator, log):
    """ CMO """
    with csv_reader('cci+cmo+cog.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
