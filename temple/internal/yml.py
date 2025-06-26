import os
import yaml
import click

class YML:
    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)

    def content(self) -> dict:
        """
        Loads and returns the parsed content of the YAML file as a dictionary.
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}
        except yaml.YAMLError as e:
            click.echo(f"YAML parsing error in '{self.path}': {e}")
            return {}

    def post(self, data: dict):
        """
        Overwrites the entire YAML file with the provided dictionary structure.
        """
        dirpath = os.path.dirname(self.path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, sort_keys=False)

        click.echo(f"{self.path} Updated")

    def put(self, key: str, value):
        """
        Update or insert a key using dot notation and save the YAML.
        """
        data = self.content()
        keys = key.split(".")
        ref = data
        for k in keys[:-1]:
            if k not in ref or not isinstance(ref[k], dict):
                ref[k] = {}
            ref = ref[k]
        ref[keys[-1]] = value

        dirpath = os.path.dirname(self.path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, sort_keys=False)

        click.echo(f"{self.path} Updated")



