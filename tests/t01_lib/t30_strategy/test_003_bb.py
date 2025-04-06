# All Pyne code must start with "@pyne" magic comment.
"""
@pyne
"""
# Import Series type
from pynecore import Series
# You can import Pine Script compatible functions and properties from pynecore.lib
from pynecore.lib import script, strategy, input, ta, plot, color


# You can define a strategy or indicator with decorator
@script.strategy("Bollinger Bands Strategy", overlay=True)
# Every Pyne code must have a main function
def main(
        # Inputs are defined in main function arguments
        source: Series[float] = input.source("close", "Source"),
        length: int = input.int(20, minval=1),
        mult: float = input.float(2.0, minval=0.001, maxval=50)
):
    basis = ta.sma(source, length)
    dev = mult * ta.stdev(source, length)
    upper = basis + dev
    lower = basis - dev

    buy_entry = ta.crossover(source, lower)
    sell_entry = ta.crossunder(source, upper)

    if buy_entry:
        strategy.entry("BBandLE",
                       strategy.long, stop=lower,
                       oca_name="BollingerBands",
                       oca_type=strategy.oca.cancel,
                       comment="BBandLE")
    else:
        strategy.cancel(id="BBandLE")

    if sell_entry:
        strategy.entry("BBandSE",
                       strategy.short, stop=upper,
                       oca_name="BollingerBands",
                       oca_type=strategy.oca.cancel,
                       comment="BBandSE")
    else:
        strategy.cancel(id="BBandSE")

    # You can use plot function...
    plot(basis, "Basis", color=color.blue)
    # ... or return a dictionary with the values you want to plot
    return {
        "upper": upper,
        "lower": lower,
    }


# noinspection PyShadowingNames
def __test_strat_bb__(csv_reader, runner, strat_equity_comparator):
    """ Bollinger Bands """
    with csv_reader('strat_ohlcv.csv', subdir="data") as cr, \
            csv_reader('bb.csv', subdir="data") as cr_equity:
        r = runner(cr, syminfo_override=dict(timezone="US/Eastern"))
        equity_iter = iter(cr_equity)
        for i, (candle, plot, new_closed_trades) in enumerate(r.run_iter()):
            for trade in new_closed_trades:
                good_entry = next(equity_iter)
                good_exit = next(equity_iter)
                strat_equity_comparator(trade, good_entry.extra_fields, good_exit.extra_fields)
