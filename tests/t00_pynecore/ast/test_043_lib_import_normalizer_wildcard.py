"""
@pyne
"""
from pynecore.lib import *
from pynecore.lib.ta import *


def main():
    print(close, hl2, sma)


def __test_import_normalizer_wildcard__(ast_transformed_code, file_reader, log):
    """
    Import normalizer - wildcard (import *)
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
