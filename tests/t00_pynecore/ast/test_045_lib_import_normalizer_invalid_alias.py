"""
@pyne
"""
from pynecore import lib as lib2


def main():
    print(lib2.close)


def __test_import_normalizer_invalid_alias__(ast_transform, file_reader):
    """
    Import normalizer - invalid alias
    """
    import pytest

    with pytest.raises(SyntaxError):
        ast_transform()
