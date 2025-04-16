# scripts/

This directory contains **utility scripts** for the internal workings of PyneCore.

⚠️ These are *not* example scripts or user-facing code!

## Contents

- `module_property_collector.py`:
  This script automatically scans all built-in modules and collects the `module_property` decorators.
  This allows the AST transformer to process them more efficiently and generate **more optimized final code**.

These scripts are **not required to use Pyne**, they are only used for fine-tuning the internal  logic.
