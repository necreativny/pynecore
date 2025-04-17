"""
@pyne
"""
from pynecore.lib import na


def main():
    # No float() or int() calls here
    na_value = na(float)
    some_string = "This is a test"
    some_bool = True

    # This file should not get an import for safe_convert
    # since it doesn't use float() or int()


def __test_safe_convert_transformer_no_transform__(ast_transformed_code, file_reader, log):
    """ Safe Convert Transformer - No Transformation """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        log.warning("Expected code:\n%s\n", file_reader(subdir="data", suffix="_ast_modified.py"))
        raise
