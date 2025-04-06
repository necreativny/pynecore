"""
@pyne
"""
from pynecore import Series


def main():
    s: Series[int] = 1
    print(s[5])


def __test_simple_series__(ast_transformed_code, file_reader, log):
    """ Simple Series """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
