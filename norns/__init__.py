import os
import xdg
from yaml import load, dump
from UserDict import DictMixin
__version__ = '0.0.1'
__author__ = "Simon van Heeringen"

class Config(DictMixin):
    """ Configuration class. 

    State will be shared across config objects. 

    """
    
    # Store shared state, Borg pattern
    __shared_state = {}
    
    def __init__(self, name=None, config_file=None):
        """ 
        Create a Config object and read a config file.

        Either name or config_file is required.
        
        Parameters
        ----------
        name : str, optional
            name for configuration

        config_file : str, optional
            name of specific configration file
        """

        self.__dict__ = self.__shared_state
        
        # Lookup the config file according to XDG hierarchy
        if name:
            self.config_file = os.path.join(
                xdg.XDG_CONFIG_HOME, name, "{}.yaml".format(name)
                )
        elif config_file: # Read specific file
            self.config_file = config_file
        else:
            raise ValueError("please provide name or config_file")

        self.config = {}
        self.load(self.config_file)

    def load(self, path):
        """ 
        Load yaml-formatted config file.

        Parameters
        ----------
        path : str
            path to config file
        """
        with open(path) as f:
            self.config = load(f)

    def save(self):
        """ 
        Save current state of config dictionary.
        """
        with open(self.config_file, "w") as f:
            f.write(dump(self.config, default_flow_style=False))

    def __getitem__(self, key):
        return self.config.__getitem__(key)
       
    def __delitem__(self, key):
        self.config.__delitem__(key)
    
    def __setitem__(self, key, value):
        return self.config.__setitem__(key, value)

    def keys():
        return self.config.keys()

def config(name=None, config_file=None):
    return Config(name=name, config_file=config_file)

if __name__ == "__main__":
    c = config("genomepy")
    print c.config_file
    print c.get("genome_path")
    c["genome_path"] = "~/genomes"
    c["flop"] = [1,2,3]
    c.save()
