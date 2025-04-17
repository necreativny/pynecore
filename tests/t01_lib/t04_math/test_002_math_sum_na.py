"""
@pyne
"""
from pynecore import Persistent
from pynecore.lib import script, log, bar_index, math, ta, na


@script.indicator(title="Math Sum NA", shorttitle="math_sum_na")
def main():
    ina: Persistent[int] = na

    if bar_index % 3 == 2:
        ina = 1
    else:
        ina = na

    t1 = ta.sma(ina, 2)
    t2 = math.sum(ina, 2)

    if bar_index < 10:
        log.info("t1: {0}, t2: {1}", t1, t2)


def __test_math_sum_na__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ math.sum() - na """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        for i in range(6):
            next(run_iter)
