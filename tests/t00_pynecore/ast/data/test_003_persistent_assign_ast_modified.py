"""
@pyne
"""
__persistent_main_p1__ = 1
__persistent_main_p2__ = None
__persistent_main_p2___initialized__ = False
__persistent_function_vars__ = {'main': ['__persistent_main_p1__', '__persistent_main_p2__', '__persistent_main_p2___initialized__']}

def main():
    global __persistent_main_p2__, __persistent_main_p2___initialized__
    if not __persistent_main_p2___initialized__:
        __persistent_main_p2__ = __persistent_main_p1__ + 1
        __persistent_main_p2___initialized__ = True
    print(__persistent_main_p2__)
