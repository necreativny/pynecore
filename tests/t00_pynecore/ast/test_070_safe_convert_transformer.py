"""
@pyne
"""
from pynecore.lib import na


def main():
    # Test float() with NA value
    na_value = na(float)
    float_val = float(na_value)  # noqa  # Should be transformed to safe_convert.safe_float(na_value)

    # Test int() with NA value
    na_int = na(int)
    int_val = int(na_int)  # noqa  # Should be transformed to safe_convert.safe_int(na_int)

    # Test regular float() that should not cause issues
    regular_val = 3.14
    regular_float = float(regular_val)  # Should be transformed to safe_convert.safe_float(regular_val)


def __test_safe_convert_transformer__(ast_transformed_code, file_reader, log):
    """ Safe Convert Transformer """
    try:
        assert ast_transformed_code == file_reader(subdir="data", suffix="_ast_modified.py")
    except AssertionError:
        log.error("AST transformed code:\n%s\n", ast_transformed_code)
        log.warning("Expected code:\n%s\n", file_reader(subdir="data", suffix="_ast_modified.py"))
        raise
