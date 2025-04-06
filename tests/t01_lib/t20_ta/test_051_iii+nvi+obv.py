"""
@pyne
"""
from pynecore.lib import script, ta


@script.indicator(title="III, NVI, OBV Test", shorttitle="iii+nvi+obv")
def main():
    return {
        "ta.iii": ta.iii,
        "ta.nvi": ta.nvi,
        "ta.obv": ta.obv,  # This also checks the cum() method and change() method with the length of 1
    }


def __test_iii_nvi_obv__(csv_reader, runner, dict_comparator, log):
    """ III, NVI, OBV """
    with csv_reader('iii+nvi+obv.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 100:
                break
