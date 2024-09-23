# importlib allows you to inspect a module's specifications without importing it. This provides metadata about the module(like its name, location, etc.)

import importlib.util 

# Find the specification of a module : 
 
spec = importlib.util.find_spec('json')

# Get details form the specification : 

print(f"Module name : {spec.name} \n")
print(f"Moduel origin : {spec.origin} \n")

