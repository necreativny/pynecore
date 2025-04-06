"""
@pyne
"""
from pynecore import Series


def main():
    def test(length):  # noqa, not used
        s: Series[int] = 1  # noqa - The same as in the outer scope intentionally
        print(s[length])

    s = 1  # Test scope isolation, this should not be a Series
    s2: Series[float] = 0.5  # Test
    print(s2[1], s)


def __test_advanced_series__(ast_transformed_code, file_reader, log):
    """
    Advanced Series
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
