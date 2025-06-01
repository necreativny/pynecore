from pathlib import Path

from pynecore.core.script_runner import idk_forkdemo_runner
from pynecore.core.ohlcv_file import OHLCVReader


script_path = Path("./demo_pyne.py")

data_path = Path("./ccxt_BYBIT_BTC_USDT_USDT_60.ohlcv")


def main():
    with OHLCVReader(data_path) as reader:
        time_from = reader.start_datetime
        time_to = reader.end_datetime
        time_from = time_from.replace(tzinfo=None)
        time_to = time_to.replace(tzinfo=None)
        ohlcv_iter = reader.read_from(int(time_from.timestamp()), int(time_to.timestamp()))

        for plot_data in idk_forkdemo_runner(script_path, ohlcv_iter):
            print(plot_data)

main()