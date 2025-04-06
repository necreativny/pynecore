"""
@pyne
"""
from pynecore.lib import script, timeframe, syminfo


@script.indicator(title="Timeframe Basic", shorttitle="tf_basic", timeframe="60")
def main():
    import pytest

    assert timeframe.main_period == "60"

    syminfo.period = "10T"
    assert timeframe.multiplier == 10
    assert timeframe.period == "10T"
    assert timeframe.isdaily is False
    assert timeframe.isdwm is False
    assert timeframe.isintraday is True
    assert timeframe.isminutes is False
    assert timeframe.ismonthly is False
    assert timeframe.isseconds is False
    assert timeframe.isticks is True
    assert timeframe.isweekly is False

    syminfo.period = "30S"
    assert timeframe.multiplier == 30
    assert timeframe.period == "30S"
    assert timeframe.isdaily is False
    assert timeframe.isdwm is False
    assert timeframe.isintraday is True
    assert timeframe.isminutes is False
    assert timeframe.ismonthly is False
    assert timeframe.isseconds is True
    assert timeframe.isticks is False
    assert timeframe.isweekly is False

    syminfo.period = "5"
    assert timeframe.multiplier == 5
    assert timeframe.period == "5"
    assert timeframe.isdaily is False
    assert timeframe.isdwm is False
    assert timeframe.isintraday is True
    assert timeframe.isminutes is True
    assert timeframe.ismonthly is False
    assert timeframe.isseconds is False
    assert timeframe.isticks is False
    assert timeframe.isweekly is False

    syminfo.period = "D"
    assert timeframe.multiplier == 1
    assert timeframe.period == "D"
    assert timeframe.isdaily is True
    assert timeframe.isdwm is True
    assert timeframe.isintraday is False
    assert timeframe.isminutes is False
    assert timeframe.ismonthly is False
    assert timeframe.isseconds is False
    assert timeframe.isticks is False
    assert timeframe.isweekly is False
    syminfo.period = "4D"
    assert timeframe.multiplier == 4
    assert timeframe.period == "4D"

    syminfo.period = "5W"
    assert timeframe.multiplier == 5
    assert timeframe.period == "5W"
    assert timeframe.isdaily is False
    assert timeframe.isdwm is True
    assert timeframe.isintraday is False
    assert timeframe.isminutes is False
    assert timeframe.ismonthly is False
    assert timeframe.isseconds is False
    assert timeframe.isticks is False
    assert timeframe.isweekly is True

    syminfo.period = "1M"
    assert timeframe.multiplier == 1
    assert timeframe.period == "1M"
    assert timeframe.isdaily is False
    assert timeframe.isdwm is True
    assert timeframe.isintraday is False
    assert timeframe.isminutes is False
    assert timeframe.ismonthly is True
    assert timeframe.isseconds is False
    assert timeframe.isticks is False
    assert timeframe.isweekly is False
    syminfo.period = "3M"
    assert timeframe.multiplier == 3
    assert timeframe.period == "3M"

    with pytest.raises(AssertionError):
        syminfo.period = "3Y"
        assert timeframe.multiplier == 1

    with pytest.raises(AssertionError):
        syminfo.period = "5X"
        assert timeframe.change("1D")


def __test_timeframe_basic__(runner, dummy_ohlcv_iter):
    """ Basic """
    next(runner(dummy_ohlcv_iter).run_iter())
