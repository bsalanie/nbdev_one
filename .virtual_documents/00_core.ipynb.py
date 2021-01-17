# default_exp core
get_ipython().run_line_magic("load_ext", " autoreload")
get_ipython().run_line_magic("autoreload", " 2")


#hide
from nbdev.showdoc import *


#export
def whoami(name: str="Bernard"):
    """
    tells you who you are
    
    @param str name: your name 
    
    @return nothing
    """
    print(f"You must be {name}.")


whoami()


help(whoami)


#export
class GuessWho:
    "a guessing interface"
    def __init__(self, name="Bernard"):
        self.name = name
    
    def guess(self):
        "tells the user their name"
        return whoami(self.name)
    
    


gw = GuessWho()
gw.guess()

gw_sp = GuessWho("MW")
gw_sp.guess()


show_doc(GuessWho.guess)



