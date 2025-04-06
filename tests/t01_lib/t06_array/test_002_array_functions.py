"""
@pyne
"""
from pynecore.lib import script, log, bar_index, array, order


@script.indicator(title="Array Functions", shorttitle="arr_func")
def main():
    if bar_index == 0:
        a = array.from_items(-1, -2, -3, -4, -5)
        log.info("array.abs(a): {0}", array.abs(a))
        log.info("array.avg(a): {0}", array.avg(a))  # -3

        a = array.from_items(1, 2, 4, 5, 6)
        log.info("array.binary_search(a, 4): {0}", array.binary_search(a, 4))  # 2
        log.info("array.binary_search(a, 3): {0}", array.binary_search(a, 3))  # -1
        log.info("array.binary_search_leftmost(a, 3): {0}", array.binary_search_leftmost(a, 3))  # 1
        log.info("array.binary_search_rightmost(a, 3): {0}", array.binary_search_rightmost(a, 3))  # 2

        b = array.from_items(7, 8, 9, 10)
        log.info("array.concat(a, b): {0}; a: {1}; b: {2}", array.concat(a, b), a, b)

        c = array.copy(a)
        log.info("c: {0}", c)

        log.info("array.covariance(a, b): {0,number,#.###############}", array.covariance(a, c))
        log.info("array.covariance(a, b, biased=false): {0,number,#.###############}",
                 array.covariance(a, c, biased=False))

        # This does not work currently, Pine Script bug!
        # log.info("array.every(a): {0}", array.every(a))  # true
        array.insert(a, 0, 0)
        # log.info("array.every(a): {0}", array.every(a))  # false

        array.fill(c, 0, 1, 3)
        log.info("c: {0}", c)

        log.info("array.first(a): {0}", array.first(a))  # 0

        log.info("array.includes(a, 4): {0}", array.includes(a, 4))  # true
        log.info("array.indexof(a, 4): {0}", array.indexof(a, 4))  # 2

        log.info("array.join(a, '', ''): {0}", array.join(a, ', '))  # 0, 1, 2, 4, 5, 6, 7, 8, 9, 10

        log.info("array.last(a): {0}", array.last(a))  # 10
        log.info("array.lastindexof(a, 4): {0}", array.lastindexof(a, 4))  # 2

        log.info("array.max(a): {0}", array.max(a))  # 10
        log.info("array.min(a): {0}", array.min(a))  # 0

        log.info("array.median(a): {0}", array.median(a))  # 5.5
        log.info("array.mode(a): {0}", array.mode(a))  # 0

        log.info("array.percentrank(a, 4): {0}", array.percentrank(a, 4))  # 0.5

        log.info("array.percentile_linear_interpolation(a, 0.5): {0}",
                 array.percentile_linear_interpolation(a, 0.5))
        log.info("array.percentile_linear_interpolation(a, 50): {0}",
                 array.percentile_linear_interpolation(a, 50))
        log.info("array.percentile_linear_interpolation(a, 70): {0}",
                 array.percentile_linear_interpolation(a, 70))

        log.info("array.percentile_nearest_rank(a, 0.5): {0}",
                 array.percentile_nearest_rank(a, 0.5))
        log.info("array.percentile_nearest_rank(a, 50): {0}",
                 array.percentile_nearest_rank(a, 50))
        log.info("array.percentile_nearest_rank(a, 70): {0}",
                 array.percentile_nearest_rank(a, 70))

        log.info("array.range(a): {0}", array.range(a))

        array.remove(a, 4)
        log.info("array.remove(a, 4): {0}", a)

        array.reverse(c)
        log.info("array.reverse(c): {0}", c)

        log.info("array.shift(a): {0}", array.shift(a))
        log.info("array.size(a): {0}", array.size(a))

        # Slice
        sa = array.slice(a, 1, 3)
        log.info("array.slice(a, 1, 3): {0}", sa)
        log.info("array.size(sa): {0}", array.size(sa))
        array.set(sa, 1, 11)
        log.info("array.set(sa, 1, 11): {0}; a: {1}", sa, a)

        # This does not work currently, Pine Script bug!
        # log.info("array.some(a): {0}", array.some(a))  # true

        array.sort(a, order.descending)
        log.info("array.sort(a, order.descending): {0}", a)
        array.sort(a, order.ascending)
        log.info("array.sort(a, order.ascending): {0}", a)

        log.info("array.sort_indices(c): {0}", array.sort_indices(c))
        log.info("array.sort_indices(c, order.descending): {0}", array.sort_indices(c, order.descending))

        log.info("array.standardize(a): {0}", array.standardize(a))
        af = array.from_items(1.1, 2.2, 3.3, 4.4, 5.5)
        log.info("array.standardize(a): {0}", array.standardize(af))

        log.info("array.stdev(a): {0,number,#.#############}", array.stdev(a))
        log.info("array.stdev(a, biased=false): {0,number,#.#############}", array.stdev(a, False))

        log.info("array.sum(a): {0}", array.sum(a))

        array.unshift(a, 0)
        log.info("array.unshift(a, 0): {0}", a)

        log.info("array.variance(a): {0,number,#.#############}", array.variance(a))
        log.info("array.variance(a, biased=false): {0,number,#.#############}", array.variance(a, False))


def __test_array_func__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ Functions """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        next(run_iter)
