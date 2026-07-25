"""
This file will have logic for the following :
check current version , and update 

"""
from koushin.config.config import read_config

class Updater:
    def __init__(self) -> None:
        pass
    
    def check_verison(self):
        """ 
            This method will check the version of current project 

            Returns:

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

        return local_metadata 
update = Updater()
print(update.check_verison())
print(update.update())
