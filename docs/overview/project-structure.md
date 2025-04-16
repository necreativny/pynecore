<!--
---
weight: 106
title: "Project Structure"
description: "Overview of the PyneCore project structure and architecture"
icon: "account_tree"
date: "2025-04-03"
lastmod: "2025-04-03"
draft: false
toc: true
categories: ["Overview", "Architecture"]
tags: ["project-structure", "architecture", "organization", "components", "modules"]
---
-->

# Project Structure

PyneCore is organized in a modular structure that allows for clean separation of concerns and extension points. This page provides a high-level overview of the project's architecture and main components.

## Repository Organization

The PyneCore repository is organized as follows:

```
pynecore/
├── src/                  # Source code
│   └── pynecore/         # Main package
│       ├── core/         # Core functionality and runtime components
│       ├── lib/          # Pine Script compatible function library
│       ├── transformers/ # AST transformers for Pine Script syntax
│       ├── types/        # Type definitions and interfaces
│       ├── utils/        # Utility functions and helpers
│       ├── cli/          # Command-line interface
│       └── providers/    # Data providers and integrations
├── tests/                # Test suite
├── docs/                 # Component-specific documentation
└── scripts/              # Utility scripts
```

## Core Components

### Core Module

The heart of the PyneCore system, implementing the fundamental data structures and execution model:

- **Series Implementation**: The core data structure that emulates Pine Script's series behavior
- **Script Runner**: Executes Pyne scripts bar-by-bar
- **Import Hook System**: Allows Python to process Pyne scripts with AST transformations
- **Data Handling**: OHLCV and CSV file operations

### Transformers Module

Python Abstract Syntax Tree (AST) transformers that modify Python code to behave like Pine Script:

- **Series Transformations**: Convert Python operations to Series-aware operations
- **Persistent Variables**: Implement persistent variables
- **Function Isolation**: Create isolated function scopes
- **Import Management**: Organize and normalize imports

### Library Module

Full Pine Script function library implemented in Python:

- **Technical Analysis**: Indicators and technical analysis functions
- **Math Functions**: Mathematical operations
- **Array Handling**: Array manipulation functions
- **Timeframe Functions**: Timeframe management
- **Chart Elements**: Chart objects and visualization

### Types Module

Type definitions for Pine Script compatible constructs:

- **Series Types**: Type definitions for Series objects
- **NA Value**: Not Available value handling
- **Persistent Types**: Persistent variable type definitions
- **Color Types**: Color handling

## Script Execution Flow

PyneCore processes and executes scripts through several stages:

1. **Script Recognition**: Scripts with the `@pyne` magic comment are recognized
2. **AST Transformation**: Python code is transformed to emulate Pine Script behavior
3. **Series Operations**: Operations are vectorized to work on time series data
4. **Bar-by-Bar Execution**: Scripts are executed one bar at a time

## Key Features

- **Pine Script Compatibility**: Familiar syntax and behavior for TradingView users
- **AST Transformations**: Uses Python's AST to implement Pine Script-like features
- **High Performance**: Optimized implementation for efficient backtesting
- **Minimal Dependencies**: Limited external package requirements
- **Comprehensive Testing**: Extensive test suite ensuring compatibility

For more detailed information about specific components, see the relevant sections in the documentation.