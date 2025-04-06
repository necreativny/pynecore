"""
@pyne
"""
from pynecore.lib import script, ta, close


@script.indicator(title="COG Test", shorttitle="COG_T", overlay=False)
def main():
    return {
        # This also tests the dev() function
        "ta.cog(close, 21)": ta.cog(close, 21),
    }


def __test_cog__(csv_reader, runner, dict_comparator, log):
    """ COG """
    with csv_reader('cci+cmo+cog.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
