# If I've imported a module and later modify its source code, Python does not automatically re-import it. However, you can reload the module without restarting the interpreter by using importlib.reload() . 

import importlib 
import mymodule # Import a module 

# Reload the module after changes : 
importlib.reload(mymodule)


