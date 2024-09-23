# In this file we shall learn about the use of Import.util.from_spec() function . 

import importlib.util 

spec = importlib.util.find_spec("os")

#  Create a module object from the spec : 

os_module = importlib.util.module_from_spec(spec)

# Load the module (execute its code) : 
spec.loader.exec_module(os_module)

# Now you can use the module as if it was imported : 
print(os_module_getcwd())  


