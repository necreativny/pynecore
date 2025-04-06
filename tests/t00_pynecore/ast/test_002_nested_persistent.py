"""
@pyne
"""
from pynecore import Persistent


def main():
    p: Persistent[float] = 1
    p += 1

    def test():  # noqa - Not used
        p: Persistent[float] = 1  # noqa - Same name as outer scope
        p += 1
        return p


def __test_nested_persistent__(ast_transformed_code, file_reader, log):
    """ Persistent in nested function """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
