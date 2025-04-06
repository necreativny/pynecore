"""
@pyne
"""
from pynecore import lib
import pynecore.lib.ta

def main():
    print(lib.close, lib.hl2, lib.ta.sma() if hasattr(lib.ta.sma, '__module_property__') else lib.ta.sma)
