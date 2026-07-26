"""
This file will have logic for the following :
check current version , and update 

"""

from koushin.config.config import (
    read_config, get_config,
    conversion
)
import requests , zipfile,io,shutil,os
from pathlib import Path
import subprocess

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

    def check_update(self)->bool:
        """
            This method will check for an update
            if there is an update then it will return True else False

        """
        local_metadata = read_config()
        cloud_metadata = get_config()
        local_version = local_metadata.get("version","")
        cloud_version = cloud_metadata.get("version","") #type:ignore 
        if conversion(cloud_version) > conversion(local_version):
            return True
        else: 
            return False
    def _doownload(self):
        """
        Thin internal method will download the project:
        1) reads the local config
        2) gets the repo from the local config
        3) gets the local_installation_path
        4) extracts owner and repo(name) from the repo url
        5) creates a zip url
        6) sends a get request to that url
        7) if not status_code == 200 raise exception
        8) reads the raw bytes from github using io.BytesIO (in-memory file)
        9) extracts all content into a clean temp dir
        10) verifies the expected extracted folder actually exists
        11) only then removes the already-installed project
        12) moves the content from temp to local installation_path
        13) removes the temp dir
        """

        if os.path.exists("temp_extraction"):
            shutil.rmtree("temp_extraction")

        local_metadata = read_config()
        repo = local_metadata.get("github")
        loacl_installation_path = Path.home() / local_metadata.get("install_path") #type:ignore
        owner, repo = repo.strip("/").split("/")[-2:] #type:ignore
        zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip"

        response = requests.get(zip_url)
        if response.status_code != 200:
            raise Exception("Could not find the main branch")

        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall("temp_extraction")

        extracted_folder = os.path.join("temp_extraction", f"{repo}-main")

        if not os.path.exists(extracted_folder):
            actual = os.listdir("temp_extraction")
            shutil.rmtree("temp_extraction")
            raise Exception(
                f"Download/extraction failed — expected '{extracted_folder}' "
                f"but found {actual}. Existing installation left untouched."
            )

        if os.path.exists(loacl_installation_path):
            shutil.rmtree(loacl_installation_path)

        shutil.move(extracted_folder, loacl_installation_path)
        shutil.rmtree("temp_extraction")
        subprocess.run(['uv', 'sync'], cwd=loacl_installation_path, check=True)

    def update(self):
        """
            This method will update the projetc to the latest available version 
        """
        if self.check_update():
            try:
                self._doownload()
            except Exception as e:
                print(f"Update failed: {e}")
                print("Existing installation was not touched.")
        else:
            print("Update not available")
       
