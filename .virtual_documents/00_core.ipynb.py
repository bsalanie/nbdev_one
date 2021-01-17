# default_exp core
get_ipython().run_line_magic("load_ext", " autoreload")
get_ipython().run_line_magic("autoreload", " 2")


#hide
from nbdev.showdoc import *


#export
def whoami(name: str="Bernard"):
    print(f"You must be {name}.")


whoami()


from nbdev.export import notebook2script; notebook2script()



