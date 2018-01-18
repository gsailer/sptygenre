import platform
import sys

if not (2, 7) <= sys.version_info:
    sys.exit(
        'ERROR: sptgenre requires Python 2.7, but found {}.'.format(platform.python_version()))

__version__ = '1.0.0b1'