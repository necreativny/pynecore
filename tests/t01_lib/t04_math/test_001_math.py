"""
@pyne
"""
from pynecore.lib import script, bar_index, math, log


@script.indicator(title="Math", shorttitle="math")
def main():
    if bar_index == 0:
        log.info("{0}", math.abs(-1))  # 1
        log.info("{0,number,#.##########}", math.acos(0.5))  # 1.0471975511965979
        log.info("{0,number,#.##########}", math.asin(0.5))  # 0.5235987755982989
        log.info("{0,number,#.##########}", math.atan(0.5))  # 0.4636476090008061
        log.info("{0}", math.avg(1, 2, 3))  # 2
        log.info("{0}", math.ceil(1.5))  # 2
        log.info("{0,number,#.##########}", math.cos(0.5))  # 0.8775825618903728

        log.info("{0,number,#.##########}", math.exp(0.5))  # 1.6487212707001282
        log.info("{0}", math.floor(1.5))  # 1
        log.info("{0,number,#.##########}", math.log(2.718281828459045))  # 1.0
        log.info("{0,number,#.##########}", math.log10(100))  # 2.0
        log.info("{0}", math.max(1, 2, 3))  # 3
        log.info("{0}", math.min(1, 2, 3))  # 1
        log.info("{0,number,#.##########}", math.pow(2, 3))  # 8.0
        log.info("{0,number,#.################}", math.random(0, 10, 1337))

        log.info("{0,number,#.##########}", math.round(1.5))  # 2
        log.info("{0,number,#.##########}", math.round(1.56789, 2))  # 1.57
        log.info("{0,number,#.##########}", math.round_to_mintick(1.56789918))  # 1.5679
        log.info("{0,number,#.##########}", math.sign(-1.5))  # -1
        log.info("{0,number,#.##########}", math.sign(1.5))  # 1
        log.info("{0,number,#.##########}", math.sign(0))  # 0

        log.info("{0,number,#.##########}", math.sin(0.5))  # 0.479425538604203
        log.info("{0,number,#.##########}", math.sqrt(4))  # 2.0
        log.info("{0,number,#.##########}", math.sqrt(-4))  # NaN

        log.info("{0,number,#.##########}", math.tan(0.5))  # 0.5463024898437905
        log.info("{0,number,#.##########}", math.todegrees(0.5))  # 28.64788975654116
        log.info("{0,number,#.##########}", math.toradians(30))  # 0.5235987755982988


def __test_math__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ Functions """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        next(run_iter)
