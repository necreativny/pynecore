"""
@pyne
"""
from pynecore.core.series import SeriesImpl
from pynecore import lib
import pynecore.lib.ta
from pynecore.core.function_isolation import isolate_function
__series_main_e__ = SeriesImpl()
__series_function_vars__ = {'main': ['__series_main_e__']}
__scope_id__ = ''

def main():
    global __scope_id__
    e = __series_main_e__.add(isolate_function(lib.ta.ema, 'main|lib.ta.ema|0', __scope_id__)(lib.close, 9))
    print(__series_main_e__[1])
