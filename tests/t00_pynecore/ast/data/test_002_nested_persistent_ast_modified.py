"""
@pyne
"""
__persistent_main_p__ = 1
__persistent_main_test_p__ = 1
__persistent_function_vars__ = {'main': ['__persistent_main_p__'], 'main.test': ['__persistent_main_test_p__']}

def main():
    global __persistent_main_p__
    __persistent_main_p__ += 1

    def test():
        global __persistent_main_test_p__
        __persistent_main_test_p__ += 1
        return __persistent_main_test_p__
