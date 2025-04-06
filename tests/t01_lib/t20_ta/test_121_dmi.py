"""
@pyne
"""
from pynecore.lib import script, ta


@script.indicator(title="DMI Test", shorttitle="dmi", overlay=False)
def main():
    dip, dim, adx = ta.dmi(17, 14)
    return {
        "ta.dmi(17, 14).dip": dip,
        "ta.dmi(17, 14).dim": dim,
        "ta.dmi(17, 14).adx": adx,
    }


def __test_dmi__(csv_reader, runner, dict_comparator, log):
    """ DMI """
    with csv_reader('dmi.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)  # I cannot make it more precise
            if i > 200:
                break
