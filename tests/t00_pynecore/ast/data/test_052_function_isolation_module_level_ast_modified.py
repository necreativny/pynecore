"""
@pyne
"""
from pynecore.core.series import SeriesImpl
from pynecore.core.function_isolation import isolate_function
__series_t1·a__ = SeriesImpl()
__series_t2·a__ = SeriesImpl()
__series_function_vars__ = {'t1': ['__series_t1·a__'], 't2': ['__series_t2·a__']}
__scope_id__ = ''

def t1():
    a = __series_t1·a__.add(1)
    a = __series_t1·a__.set(a + 1)
    return __series_t1·a__[1]

def t2():
    a = __series_t2·a__.add(1)
    a = __series_t2·a__.set(a + 1)
    return __series_t2·a__[1]

def main():
    global __scope_id__
    a = isolate_function(t1, 'main|t1|0', __scope_id__)()
    print(a)
    b = isolate_function(t1, 'main|t1|1', __scope_id__)()
    print(b)
    c = isolate_function(t2, 'main|t2|2', __scope_id__)()
    print(c)
