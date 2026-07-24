"""
This file will be responsible for creating config.koushin 

Note:   working on to create reading config.koushin


"""
from pathlib import Path
import configparser


def create_config(github:str,path = Path.cwd()):
    """ 
    This function will create config.koushin which will contain the following
    
    ARGS:
    
    github : github link forr the project 
    path : path to create config file deafults to current working dir 

    """
    repo = github or "https://github.com/Shishir-Kc/Koushin" 
    version_manager = f"{repo}/config.koushin"
    TEMPLATE = f"""
    
[github]
repo = {repo}
[version]
version-manager = {version_manager}
version = 0.0.1
     
"""
    with open(f"{path}/config.koushin","w")as file:
        file.write(TEMPLATE)        

def read_config(path = Path.cwd()):
    """
    
    This function will read config.koushin and will return the following:
    
    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw file 

    version : current version 

    """

    config= configparser.ConfigParser()
    config.read(f"{path}/config.koushin")
    return {
        "github":config["github"]["repo"],
        "version-manager":config["version"]["version-manager"],
        "version":config["version"]["version"]
    }

# create_config(github="https://github.com/Shishir-Kc/Koushin")
read_config()
