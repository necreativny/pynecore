"""
@pyne
"""
import pynecore.lib.ta as ta


def main():
    print(ta)


def __test_import_normalizer_global_alias__(ast_transformed_code, file_reader, log):
    """
    Import normalizer - global alias
    """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        raise
