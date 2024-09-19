# This shall give a rough idea regarding the importlib module in Python :

# This library is generally used to, customize and work in a better way with the import library in Python.

import importlib


# Dynamically import a module using its name as a string

importing_module = importlib.import_module("math")

print(importing_module.sqrt(16))


