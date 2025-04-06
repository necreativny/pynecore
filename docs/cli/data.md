<!--
---
weight: 303
title: "Data Management"
description: "Managing OHLCV data with the PyneCore CLI"
icon: "database"
date: "2025-04-03"
lastmod: "2025-04-03"
draft: false
toc: true
---
-->

# Data Management

The PyneCore CLI provides a set of commands for managing OHLCV (Open, High, Low, Close, Volume) data. These commands allow you to download historical data from various providers, convert between formats, and manage your local data files.

## Data Commands Overview

The data commands are organized under the `data` subcommand:

```bash
pyne data [COMMAND] [OPTIONS] [ARGUMENTS]
```

Available data commands:
- `download`: Download historical OHLCV data from a provider
- `convert-to`: Convert PyneCore format to other formats (CSV, JSON)
- `convert-from`: Convert other formats to PyneCore format

## Downloading Data

The `download` command allows you to fetch historical OHLCV data from various providers.

### Basic Usage

```bash
pyne data download PROVIDER [OPTIONS]
```

Where `PROVIDER` is one of the available data providers.

### Available Providers

PyneCore currently supports the following data providers:
- `ccxt`: CCXT library for accessing cryptocurrency exchanges
- `capitalcom`: Capital.com market data

To see which providers are available in your installation, use:

```bash
pyne data download --help
```

### Download Options

- `--symbol`, `-s`: Symbol to download (e.g., "BINANCE:BTC/USDT" for CCXT)
- `--timeframe`, `-tf`: Timeframe in TradingView format (1, 5, 15, 30, 60, 240, 1D, 1W)
- `--from`, `-f`: Start date or days back from now, or 'continue' to resume last download
- `--to`, `-t`: End date or days from start date
- `--list-symbols`, `-ls`: List available symbols of the provider
- `--symbol-info`, `-si`: Show symbol information
- `--force-save-info`, `-fi`: Force save symbol information
- `--truncate`, `-tr`: Truncate file before downloading (all data will be lost)

### Download Examples

```bash
# List all available symbols from CCXT provider
pyne data download ccxt --list-symbols

# Download Bitcoin daily data from CCXT, continuing from last download
pyne data download ccxt --symbol "BINANCE:BTC/USDT" --timeframe "1D"

# Download Forex 1-hour data from Capital.com for a specific date range
pyne data download capitalcom --symbol "EURUSD" --timeframe "60" --from "2023-01-01" --to "2023-12-31"

# Download data for the last 90 days
pyne data download ccxt --symbol "BINANCE:ETH/USDT" --timeframe "1D" --from "90"

# Truncate existing data and download everything again
pyne data download ccxt --symbol "BINANCE:BTC/USDT" --timeframe "1D" --truncate
```

### Understanding Date Formats

The `--from` and `--to` options accept several formats:

1. **ISO date format**: `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`
   ```bash
   --from "2023-01-01" --to "2023-12-31 23:59:59"
   ```

2. **Number of days** (for `--from` only): Number of days back from now
   ```bash
   --from "90"  # Last 90 days
   ```

3. **"continue"** (for `--from` only): Continue from the last downloaded point
   ```bash
   --from "continue"
   ```

If `--from` is not specified, it defaults to "continue" (or one year if no data exists).
If `--to` is not specified, it defaults to the current date and time.

### Symbol Information

When downloading data, PyneCore also fetches and stores symbol information in a TOML file. This includes:
- Full symbol name and description
- Exchange details
- Trading hours
- Tick size and value
- Contract specifications (for futures)

You can view this information with the `--symbol-info` flag:
```bash
pyne data download ccxt --symbol "BINANCE:BTC/USDT" --timeframe "1D" --symbol-info
```

## Converting Data Formats

PyneCore uses a binary format (`.ohlcv`) for storing OHLCV data efficiently. However, you can convert this data to and from other formats for interoperability.

### Converting to Other Formats

The `convert-to` command converts PyneCore format to CSV or JSON:

```bash
pyne data convert-to PROVIDER [OPTIONS]
```

Options:
- `--symbol`, `-s`: Symbol to convert
- `--timeframe`, `-tf`: Timeframe in TradingView format
- `--format`, `-f`: Output format (csv, json)
- `--as-datetime`, `-dt`: Save timestamp as datetime instead of UNIX timestamp

Example:
```bash
# Convert Bitcoin data to CSV
pyne data convert-to ccxt --symbol "BINANCE:BTC/USDT" --timeframe "1D" --format "csv"

# Convert with human-readable dates
pyne data convert-to ccxt --symbol "BINANCE:BTC/USDT" --timeframe "1D" --format "csv" --as-datetime
```

### Converting from Other Formats

The `convert-from` command converts CSV or JSON format to PyneCore format:

```bash
pyne data convert-from FILE_PATH [OPTIONS]
```

Where `FILE_PATH` is the path to the CSV or JSON file to convert.

Options:
- `--provider`, `-p`: Data provider name (can be any name, defaults to "custom")
- `--symbol`, `-s`: Symbol name
- `--timeframe`, `-tf`: Timeframe in TradingView format
- `--fmt`, `-f`: Input format (csv, json) - defaults to the file extension if not specified
- `--timezone`, `-tz`: Timezone of the timestamps (defaults to UTC)

Example:
```bash
# Convert CSV to PyneCore format
pyne data convert-from ./data/btcusd.csv --symbol "CUSTOM:BTC/USD" --timeframe "1D"

# Convert with timezone specification
pyne data convert-from ./data/eurusd.csv --symbol "CUSTOM:EUR/USD" --timeframe "60" --timezone "Europe/London"
```

## Data File Structure

PyneCore uses a structured approach to store OHLCV data:

### File Locations

Data files are stored in the `workdir/data/` directory with standardized naming:
```
<provider>_<symbol>_<timeframe>.ohlcv   # OHLCV data file
<provider>_<symbol>_<timeframe>.toml    # Symbol information file
```

For example:
```
ccxt_BINANCE_BTC_USDT_1D.ohlcv
ccxt_BINANCE_BTC_USDT_1D.toml
```

### OHLCV File Format

The `.ohlcv` format is a binary format optimized for:
- Fast reading and writing
- Compact storage
- Efficient bar-by-bar access
- Support for time range queries

When converted to CSV, the format has the following columns:
```
timestamp,open,high,low,close,volume
```

## Advanced Usage

### Working with Large Datasets

When working with large datasets, consider:

1. **Incremental downloads**: Use the `--from "continue"` option to download only new data
2. **Date range restriction**: Use `--from` and `--to` to download specific periods
3. **Date filters in scripts**: Apply time filters in your scripts to process only relevant data


## Provider-Specific Information

### CCXT Provider

The CCXT provider uses the [CCXT library](https://github.com/ccxt/ccxt) to connect to various cryptocurrency exchanges.

Symbol format for CCXT: `EXCHANGE:BASE/QUOTE`, for example `BINANCE:BTC/USDT`.

Available exchanges depend on the CCXT library, which supports 100+ cryptocurrency exchanges.

### Capital.com Provider

The Capital.com provider connects to the Capital.com API for forex, stocks, indices, and more.

Symbol format for Capital.com: `SYMBOL`, for example `EURUSD`.

## Troubleshooting

### Download Issues

If you encounter issues when downloading data:

1. **Connection errors**: Check your internet connection and try again
2. **Provider issues**: The provider might be temporarily unavailable, try later
3. **Rate limiting**: You might be hitting rate limits, slow down your requests
4. **Authentication**: Some providers require authentication - check the configuration in `workdir/config/`

### Format Conversion Issues

When converting formats:

1. **CSV format issues**: Ensure your CSV has the correct columns (timestamp, open, high, low, close, volume)
2. **Timestamp format**: Make sure timestamps are in the expected format (UNIX timestamp or ISO format)
3. **Timezone issues**: Specify the correct timezone with `--timezone` when converting from external sources

### Missing Symbol Information

If symbol information is missing:

1. **Force update**: Use `--force-save-info` to fetch new symbol information
2. **Manual creation**: Create a TOML file manually following the expected format
3. **Provider support**: Some providers might not support all symbols or have limited information
