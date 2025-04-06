"""
@pyne
"""
from pynecore.core.series import SeriesImpl
__series_main_s__ = SeriesImpl()
__series_function_vars__ = {'main': ['__series_main_s__']}

def main():
    s = __series_main_s__.add(1)
    print(__series_main_s__[5])
