"""
This file will have logic for the following :
check current version , and update 

"""
from re import sub
from src.koushin.config.config import (
    read_config, get_config,
    conversion, generate_clean_path 
)
import subprocess
import os
from pathlib import Path
import shutil


class Updater:
    def __init__(self) -> None:
        pass
    
    def check_verison(self):
        """ 
            This method will check the version of current project 

            Returns: (eg)

            {
            'current_version':'0.0.1'
            }

        """
        project_metadata= read_config()
        return {
            "current_version":project_metadata.get("version","")
        }

    def update(self):
        """
            This method will update the projetc to the latest available version 
        """
        local_metadata = read_config()
        cloud_metadata = get_config()
        github_repo = cloud_metadata.get("github","") #type:ignore
        installation_path = cloud_metadata.get("install_path") #type:ignore
        local_version = local_metadata.get("version","")
        cloud_version = cloud_metadata.get("version","") #type:ignore 
        if conversion(cloud_version) > conversion(local_version):
            local_installation_path = local_metadata.get("install_path","")
            project_name = local_metadata.get("project_name","")
            installation_path = generate_clean_path(path=local_installation_path,project_name=project_name)
            print(f"new update will be installed for {project_name} on {installation_path} form repo {github_repo}")
            for entry in os.scandir(local_installation_path):
                if entry.is_dir(follow_symlinks=False):
                    shutil.rmtree(entry.path)
            os.chdir(os.path.expanduser("~"))
            subprocess.run(f"git clone {github_repo} {installation_path}",shell=True)
            os.chdir(local_installation_path)
            subprocess.run("uv sync",shell=True)

