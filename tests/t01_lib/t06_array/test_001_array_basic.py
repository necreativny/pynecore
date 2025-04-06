"""
@pyne
"""
from pynecore.lib import script, log, bar_index, array, color


@script.indicator(title="Array Basic", shorttitle="arr_basic")
def main():
    if bar_index == 0:
        ab = array.new_bool(5, False)
        ac = array.new_color(5, color.red)
        af = array.new_float(5, 0.0)
        ai = array.new_int(5, 0)
        as_ = array.new_string(5, "s")

        array.set(ab, 0, True)
        # array.set(ab, -2, True)  # This does not work currently, Pine Script bug!
        array.set(ac, 0, color.green)
        array.set(ac, -2, color.orange)
        array.set(af, 0, 1.0)
        array.set(af, -2, 2.0)
        array.set(ai, 0, 1)
        array.set(ai, -2, 2)
        array.set(as_, 0, "s0")
        array.set(as_, -2, "s2")

        log.info("ab: {0}", ab)
        # Pine can't log color arrays, so we compare them here
        log.info("ac[3]: {0}", array.get(ac, 3) == color.orange)
        log.info("ac[0]: {0}", array.get(ac, 0) == color.green)
        log.info("af: {0}", af)
        log.info("ai: {0}", ai)
        log.info("as_: {0}", as_)

        a = array.from_items(-1, -2, -3, -4, -5)
        log.info("a: {0}", a)
        log.info("array.size(a): {0}", array.size(a))
        array.push(a, 6)
        log.info("array.pop(a, 0): {0}", array.pop(a))
        log.info("array.size(a): {0}", array.size(a))

        array.clear(a)
        log.info("array.size(a): {0}", array.size(a))  # 0


def __test_array__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ Basic """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        next(run_iter)
