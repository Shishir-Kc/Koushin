"""
This file will be responsible for creating config.koushin 

Note:   working on to create reading config.koushin


"""
from pathlib import Path


def create_file(github:str,path = Path.cwd()):
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


create_file(github="https://github.com/Shishir-Kc/Koushin")

