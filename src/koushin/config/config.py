"""
This file will be responsible for creating config.koushin 

"""
from pathlib import Path
import configparser
import requests

def generate_raw_github_content(github:str):
   """  
        This fucntion will generate raw github content for config.koushin
   """
   koushin_path = f"{github.replace("github","raw.githubusercontent")}/refs/heads/main/config.koushin"
   return koushin_path

def create_config(github:str,path = Path.cwd()):
    """ 
    This function will create config.koushin which will contain the following
    
    ARGS:
    
    github : github link forr the project 
    path : path to create config file deafults to current working dir 

    """
    repo = github or "https://github.com/Shishir-Kc/Koushin" 
    version_manager = generate_raw_github_content(github)
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
    
    This function will read config.koushin (Local)  and will return the following:
    
    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url  

    version : current version 

    """

    config= configparser.ConfigParser()
    config.read(f"{path}/config.koushin")
    return {
        "github":config["github"]["repo"],
        "version-manager":config["version"]["version-manager"],
        "version":config["version"]["version"]
    }


def get_config():
    """ 
    This function will get the cloud (github) config.koushin

    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url 

    version : cloud (github) version 

    """
    config = configparser.ConfigParser()
    raw_config_url = str(read_config().get("version-manager"))
    try:
        response = requests.get(raw_config_url)
        if response.status_code == 200:
            config.read_string(response.text)
            return {
             "github":config["github"]["repo"],
             "version-manager":config["version"]["version-manager"],
             "version":config["version"]["version"]
    }
    except Exception as e:
        print(e)


