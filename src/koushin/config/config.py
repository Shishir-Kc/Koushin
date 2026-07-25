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

def create_config(github:str,project_name:str):
    """ 
    This function will create config.koushin which will contain the following
    
    ARGS:
    
    github : github link forr the project 
     
    project_name : name of the project 

    project_path : path where client will install the project (by default it will be default val developer will have to add the project_path for client ) 
    
    Hint:

        when client runs the project for the first time it is suggested to add project_path 
        use add_install_path(path) function .
    """
    path = Path.cwd()
    repo = github or "https://github.com/Shishir-Kc/Koushin" 
    version_manager = generate_raw_github_content(github)
    install_path = "path/where/user/will/install/this/project"
    TEMPLATE = f""" 
[github]
repo = {repo}
[project]
name = {project_name}
[version]
version-manager = {version_manager}
version = 0.0.1 
[path]
install-path = {install_path}
"""
    with open(f"{path}/config.koushin","w")as file:
        file.write(TEMPLATE)        

def read_config():
    """
    
    This function will read config.koushin (Local)  and will return the following:
    
    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url  

    version : current version 
    
    project_name : name of the project 

    """

    config= configparser.ConfigParser()
    config.read(f"{Path.cwd()}/config.koushin")
    return {
        "github":config["github"]["repo"],
        "version-manager":config["version"]["version-manager"],
        "version":config["version"]["version"],
        "install_path":config["path"]["install-path"],
        "project_name": config["project"]["name"]
    }

def add_install_path(path):
    """
        This function will add the installation path of the client machine use this when 
        the main code runs in client machine for the first time ! , by default it will have  ' home/username '
        full path specification is suggested.
    """

    config = configparser.ConfigParser()
    config.read(f"{Path.cwd()}/config.koushin")
    installation_path = str(Path.home() / path)

    config.set('path','install-path',installation_path)
    with open(f"{Path.cwd()}/config.koushin","w") as configfile:
        config.write(configfile)


def get_config():
    """ 
    This function will get the cloud (github) config.koushin

    Returns:
    
    github : github repo for the project 

    version-manager : will return config.kosun raw github url 

    version : cloud (github) version 

    project_name : name of the project 
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
             "version":config["version"]["version"],
             "install_path":config["path"]["install-path"],
             "project_name": config["project"]["name"]   
           }
    

    except Exception as e:
        print(e)

def conversion(v):
    """ 
        This will convert str to int using map  
    """
    return tuple(map(int,v.split(".")))

def generate_clean_path(path:str,project_name)->str:
    """
      This function will generate a clean path where the project lives
      suppose if a project is on path .config/os/koushin then this function 
      will return .config/os . 

    ARGS:

    path : full path where the project is installed on client side 

    project_name : project name (it should not be differ )


    """
    return path.replace(f"/{project_name}","")

    
# print(generate_clean_path(path="/home/x64_x86/.config/koushin",project_name="koushin"))

# add_install_path(".config/koushin")
# create_config(github="https://github.com/Shishir-Kc/Koushin",project_name="koushin")
