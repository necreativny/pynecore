"""
@pyne
"""
from pynecore import Persistent


def main():
    p1: Persistent[float] = 1
    p2: Persistent[float] = p1 + 1
    print(p2)


def __test_persistent_assign__(ast_transformed_code, file_reader, log):
    """ Persistent Assign """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
