"""
@pyne
"""
from pynecore.lib import script, log, bar_index, math


@script.indicator(title="Math Random", shorttitle="math_rnd")
def main():
    if bar_index < 5:
        log.info("bar_index: {0}; r: {1,number,#.###############}", bar_index, math.random(0, 1, 42))
        log.info("bar_index: {0}; r: {1,number,#.###############}", bar_index, math.random(0, 1, 42))


def __test_math_random__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ math.random() """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        for i in range(5):
            next(run_iter)
