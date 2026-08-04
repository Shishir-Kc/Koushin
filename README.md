### Installation
```
uv add koushin
```

### Implementation
# 1) Creating config

```
koushin generate
```

# 1.1) Adding informations

after entering **koushin generate** developer will be asked with few prompts (make sure .venv is active).
1) project name (it should be same as repo name) :
2) github repo url for the project :
3) project path where it will be installed at client side :

after this config.koushin will be generated !
with the following :

```
[github]
repo = your project repo url
[project]
name = your project name
[version]
version-manager = your project repo url/refs/heads/main/config.koushin
version = 0.0.1
[path]
install-path = client installation path

```

# 2) Implementing updater

> NOTE : as a developer you would have to create a seperate updater file where koushin will do its work. the logic should be your to update as you desire .

For normal updater developer would only have to use two methods

```
from koushin.core.koushin import Updater

my_project = Updater()

if my_project.check_verison(): # <--- checks for update if there is then it will return true else false
    my_project.update() # <--- updates your project automatically

```

Thats it ! new method will be uploaded if i need to make one for now i will be implemnting koushin to my personal projects .

## Docs for how i made it will be uploaded soon : )

### Logging

koushin now includes built-in logging. Logs are stored in a `LOG/` directory at the project root in `LOG/koushin.log`. The logger is automatically initialized when koushin is imported.

### CLI Commands

```
koushin generate    # Generate config.koushin
koushin info        # Show info
```

### Utility Functions

- `generate_clean_path(path, project_name)` — strips the project name from a full path to return the parent directory
- `add_install_path(path)` — updates the `install-path` in `config.koushin`
- `get_config()` — fetches the cloud (GitHub) config.koushin and returns metadata
- `cretate_logger_file()` — creates the `LOG/` directory and returns its path