"""
@pyne
"""
from pynecore.core.series import SeriesImpl
from pynecore import lib
__series_main·_lib_close__ = SeriesImpl()
__series_main·a__ = SeriesImpl()
__series_function_vars__ = {'main': ['__series_main·_lib_close__', '__series_main·a__']}

def main():
    _lib_close = __series_main·_lib_close__.add(lib.close)
    a = __series_main·a__.add(__series_main·_lib_close__[10])
    print(a)
