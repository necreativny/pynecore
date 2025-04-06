"""
@pyne
"""
from pynecore import Series
from pynecore.lib import close, ta


def main():
    e: Series[float] = ta.ema(close, 9)
    print(e[1])


def __test_function_isolation_lib__(log, ast_transformed_code, file_reader):
    """
    Function Isolation - lib functions
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
