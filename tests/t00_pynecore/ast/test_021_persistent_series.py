"""
@pyne
"""
from pynecore import PersistentSeries, Persistent, Series


def main():
    def t(length):  # noqa, not used
        s: PersistentSeries[int] = 1  # noqa - The same as in the outer scope intentionally
        s += 1
        print(s, s[length])

    s = 1  # Test scope isolation, this should not be a Series
    s2: PersistentSeries[float] = 0.5  # Test
    s2 += 1
    print(s2[1], s)


def __test_advanced_series__(ast_transformed_code, file_reader, log):
    """ Persistent Series """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
