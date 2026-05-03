#!/usr/bin/env python3
# hsb.py - Hotspot Bypass Pro Launcher

import sys

try:
    import hotspot_bypass as bypass
except ImportError as e:
    print(f"Error: Could not load module - {e}")
    print("Make sure hotspot_bypass.so is in the same directory")
    sys.exit(1)

if __name__ == "__main__":
    bypass.run()
