"""
@pyne
"""
from pynecore import Series


def t2(s: Series[float], s1: Series[float]):  # noqa, not used
    s += 1
    print(s, s[1], s1, s1[10])
    return s[2]


def main():
    def t(s: Series[float]):  # noqa, not used
        s += 1
        print(s, s[1])
        return s

    s: Series[float] = 1  # noqa, not used


def __test_advanced_series__(ast_transformed_code, file_reader, log):
    """
    Argument Series
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
