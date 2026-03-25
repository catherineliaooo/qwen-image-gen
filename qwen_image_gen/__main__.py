"""
Main entry point for running as module:
python -m qwen_image_gen
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
