"""
@pyne
"""
from pynecore.core.series import SeriesImpl
__persistent_main_t_s__ = 1
__persistent_main_s2__ = 0.5
__persistent_function_vars__ = {'main.t': ['__persistent_main_t_s__'], 'main': ['__persistent_main_s2__']}
__series_main_s2__ = SeriesImpl()
__series_main_t_s__ = SeriesImpl()
__series_function_vars__ = {'main.t': ['__series_main_t_s__'], 'main': ['__series_main_s2__']}

def main():
    global __persistent_main_s2__

    def t(length):
        global __persistent_main_t_s__
        __persistent_main_t_s__ = __series_main_t_s__.add(__persistent_main_t_s__)
        __persistent_main_t_s__ = __series_main_t_s__.set(__persistent_main_t_s__ + 1)
        print(__persistent_main_t_s__, __series_main_t_s__[length])
    s = 1
    __persistent_main_s2__ = __series_main_s2__.add(__persistent_main_s2__)
    __persistent_main_s2__ = __series_main_s2__.set(__persistent_main_s2__ + 1)
    print(__series_main_s2__[1], s)
