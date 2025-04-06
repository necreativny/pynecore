"""
@pyne
"""
from pynecore.core.series import SeriesImpl
__series_main_s__ = SeriesImpl()
__series_main_t_s__ = SeriesImpl()
__series_t2_s1__ = SeriesImpl()
__series_t2_s__ = SeriesImpl()
__series_function_vars__ = {'t2': ['__series_t2_s__', '__series_t2_s1__'], 'main.t': ['__series_main_t_s__'], 'main': ['__series_main_s__']}

def t2(s: float, s1: float):
    s = __series_t2_s__.add(s)
    s1 = __series_t2_s1__.add(s1)
    s = __series_t2_s__.set(s + 1)
    print(s, __series_t2_s__[1], s1, __series_t2_s1__[10])
    return __series_t2_s__[2]

def main():

    def t(s: float):
        s = __series_main_t_s__.add(s)
        s = __series_main_t_s__.set(s + 1)
        print(s, __series_main_t_s__[1])
        return s
    s = __series_main_s__.add(1)
