import os
import json
import click

from temple import workspaces_packages
from temple.internal.yml import YML

class TempleConfig():
    def __init__(self, templefile: str = "temple.yml"):
        self.templefile = templefile

    def init(self, name: str, force: bool = False):
        self.name = name
        temple = YML(self.templefile)
        configs = {
            "group_name": self.name,
            "build": {
                ".env.dev": ".env.dev",
                ".env.prod": ".env.prod",
                ".gitignore": ".gitignore",
                "docker-compose.yml": "docker-compose.yml",
                "hermes.yml": "hermes.yml",
            },
            "workspaces": None
        }
        if ((temple.content() in [None, {}]) or force):
            temple.post(configs)
            if(force):
                click.echo(f"Temple configuration file '{self.templefile}' overwritten")
            else:
                click.echo(f"Temple configuration file '{self.templefile}' created with group name '{self.name}'.")
        else:
            click.echo(f"Temple configuration file '{self.templefile}' already exists (No changes made)")

    def add_workspace(self, workspace_name: str, workspace_type: str):
        temple = YML(self.templefile)
        workspaces = temple.content().get('workspaces', {})
        paths_json = os.path.join(workspaces_packages, workspace_type, "paths.json")

        with open(paths_json, 'r', encoding='utf-8') as f:
            paths = json.load(f)

        workspace = {
            workspace_name: {
                "workspace": workspace_type,
                "build": paths
            }
        }
        temple.put("workspaces", (workspaces or {}) | workspace)

    def read(self):
        temple = YML(self.templefile)
        configs = temple.content()
        return configs

    def update(self, key_path, value):
        temple = YML(self.templefile)
        temple.put(key_path, value)

