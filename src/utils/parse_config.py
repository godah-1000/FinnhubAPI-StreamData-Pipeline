import yaml

#get data configuration from yaml file
def get(config) -> dict:
    with open(config, encoding="utf-8") as file:
        return yaml.safe_load(file)

