"""
@pyne
"""
from pynecore import Series


def t1():
    a: Series[float] = 1  # noqa - The same as in the outer scope intentionally
    a += 1
    return a[1]


def t2():
    a: Series[float] = 1  # noqa - The same as in the outer scope intentionally
    a += 1
    return a[1]


def main():
    a = t1()
    print(a)
    b = t1()
    print(b)
    c = t2()
    print(c)


def __test_function_isolation_module_level__(log, ast_transformed_code, file_reader):
    """
    Function Isolation - module level functions
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
