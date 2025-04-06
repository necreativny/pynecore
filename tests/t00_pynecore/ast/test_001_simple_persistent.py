"""
@pyne
"""
from pynecore import Persistent


def main():
    p: Persistent[float] = 1
    p += 1


def __test_simple_persistent__(ast_transformed_code, file_reader, log):
    """ Simple Persistent """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        log.warning("Expected code:\n%s\n", file_reader(subdir="data", suffix="_ast_modified.py"))
        raise
