"""
@pyne
"""
from pynecore.lib import script, log, bar_index, math, NA


@script.indicator(title="Math Sum", shorttitle="math_sum")
def main():
    if bar_index < 5:
        log.info("{0}", math.sum(bar_index, 3))


def __test_math_sum__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ math.sum() """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        for i in range(5):
            next(run_iter)
