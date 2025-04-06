"""
@pyne
"""
from pynecore.lib import script, session, plot


@script.indicator(title="Session", shorttitle="session")
def main():
    plot(1 if session.isfirstbar else 0, "isfirstbar")
    plot(1.5 if session.isfirstbar_regular else 0, "isfirstbar_regular")
    plot(2 if session.islastbar else 0, "islastbar")
    plot(2.5 if session.islastbar_regular else 0, "islastbar_regular")
    plot(3 if session.ismarket else 0, "ismarket")


def __test_session__(csv_reader, runner, dict_comparator, log):
    """ Properties """
    from pathlib import Path
    syminfo_path = Path(__file__).parent / "data" / "session.toml"
    with csv_reader('session.csv', subdir="data") as cr:
        for candle, _plot in runner(cr, syminfo_path=syminfo_path).run_iter():
            dict_comparator(_plot, candle.extra_fields)
