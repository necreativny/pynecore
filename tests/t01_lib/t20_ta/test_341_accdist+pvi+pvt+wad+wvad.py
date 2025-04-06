"""
@pyne
"""
from pynecore.lib import script, ta, plot, color


@script.indicator(title="AccFist/PVI/PVT/WAD/WVAD Test", shorttitle="accdist+pvi+pvt+wad+wvad", overlay=True)
def main():
    plot(ta.accdist, "ta.accdist", color.white)
    plot(ta.pvi, "ta.pvi", color.yellow)
    plot(ta.pvt, "ta.pvt", color.fuchsia)  # also tests ta.cum()
    plot(ta.wad, "ta.wad", color.blue)
    plot(ta.wvad, "ta.wvad", color.navy)


# noinspection PyShadowingNames
def __test_accdist_pvi_pvt_wad_wvad__(csv_reader, runner, dict_comparator, log):
    """ AccDist / PVI / PVT / WAD / WVAD """
    with csv_reader('accdist+pvi+pvt+wad+wvad.csv', subdir="data") as cr:
        for i, (candle, plot) in enumerate(runner(cr).run_iter()):
            dict_comparator(plot, candle.extra_fields)
            if i > 150:
                break
