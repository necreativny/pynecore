"""
@pyne
"""
from pynecore import Series


def main():
    def t():
        a: Series[float] = 1  # noqa - The same as in the outer scope intentionally
        a += 1
        return a[1]

    a = t()
    print(a)
    b = t()
    print(b)


def __test_function_isolation_main_inner__(log, ast_transformed_code, file_reader):
    """
    Function Isolation - inner function in main
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
