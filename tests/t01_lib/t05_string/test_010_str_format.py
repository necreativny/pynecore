"""
@pyne
"""
from pynecore.lib import script, log, bar_index, string


@script.indicator(title="String Format", shorttitle="strfmt")
def main():
    if bar_index == 0:
        s0 = string.format("{0}", 1.23456789)  # returns: 1.234
        log.info("{0}", s0)

        # The format specifier inside the curly braces accepts certain modifiers:

        # - Specify the number of decimals to display:
        s1 = string.format("{0,number,#.#}", 1.34)  # returns: 1.3
        log.info("{0}", s1)
        # - Round a float value to an integer:
        s2 = string.format("{0,number,integer}", 1.34)  # returns: 1
        log.info("{0}", s2)
        # - Display a number in currency:
        s3 = string.format("{0,number,currency}", 1.34)  # returns: $1.34
        log.info("{0}", s3)
        # - Display a number as a percentage:
        s4 = string.format("{0,number,percent}", 0.5)  # returns: 50 %
        log.info("{0}", s4)

        # EXAMPLES WITH SEVERAL ARGUMENTS

        # returns: Number 1 is not equal to 4
        s5 = string.format("Number {0} is not {1} to {2}", 1, "equal", 4)
        log.info("{0}", s5)
        # returns: 1.34 != 1.3
        s6 = string.format("{0} != {0, number, #.#}", 1.34)
        log.info("{0}", s6)
        # returns: 1 is equal to 1, but 2 is equal to 2
        s7 = string.format("{0, number, integer} is equal to 1, but {1, number, integer} is equal to 2", 1.34, 1.52)
        log.info("{0}", s7)
        # returns: The cash turnover amounted to $1,340,000.00
        s8 = string.format("The cash turnover amounted to {0, number, currency}", 1340000)
        log.info("{0}", s8)
        # returns: Expected return is 10 % - 20 %
        s9 = string.format("Expected return is {0, number, percent} - {1, number, percent}", 0.1, 0.2)
        log.info("{0}", s9)


# noinspection PyShadowingNames
def __test_str_format__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ string.format() """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        next(run_iter)
