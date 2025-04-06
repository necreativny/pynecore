"""
@pyne
"""
from pynecore.lib import close, hl2, ta


def main():
    print(close, hl2, ta)


def __test_import_normalizer_from_import__(ast_transformed_code, file_reader, log):
    """
    Import normalizer - from import
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
