from distutils.core import setup
import sys, os, py2exe

sys.argv.append("py2exe")
setup(
    options = {'py2exe': {'bundle_file': 1}},
    
    windows = [{'script':"source_python.py"}],
    zipfile = None,
)

