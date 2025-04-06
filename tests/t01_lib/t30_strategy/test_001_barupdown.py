"""
@pyne
"""
from pynecore.lib import script, close, open, strategy, input


@script.strategy("BarUpDn Strategy", overlay=True,
                 default_qty_type=strategy.percent_of_equity,
                 default_qty_value=10)
def main(
        max_id_loss_pcnt=input.float(1, "Max Intraday Loss(%)")
):
    strategy.risk.max_intraday_loss(max_id_loss_pcnt, strategy.percent_of_equity)
    if close > open > close[1]:
        strategy.entry("BarUp", strategy.long)
    if close < open < close[1]:
        strategy.entry("BarDn", strategy.short)


# noinspection PyShadowingNames
def __test_strat_barupdown__(csv_reader, runner, strat_equity_comparator):
    """ BarUpDn """
    with csv_reader('strat_ohlcv.csv', subdir="data") as cr, \
            csv_reader('barupdown.csv', subdir="data") as cr_equity:
        r = runner(cr, syminfo_override=dict(timezone="US/Eastern"))
        equity_iter = iter(cr_equity)
        for i, (candle, plot, new_closed_trades) in enumerate(r.run_iter()):
            for trade in new_closed_trades:
                good_entry = next(equity_iter)
                good_exit = next(equity_iter)
                strat_equity_comparator(trade, good_entry.extra_fields, good_exit.extra_fields)
