import os
import json
from temple import workspaces_packages
        
class WorkspacePackage:
    def __init__(self, workspace_type: str):
        self.workspace_type = workspace_type
        self.path = os.path.join(workspaces_packages, workspace_type)

    def paths(self) -> dict:
        paths_json = os.path.join(workspaces_packages, self.workspace_type, "paths.json")
        with open(paths_json, 'r', encoding='utf-8') as f:
            paths = json.load(f)
            return paths
    
    def cmds(self) -> dict:
        cmds_json = os.path.join(workspaces_packages, self.workspace_type, "cmds.json")
        with open(cmds_json, 'r', encoding='utf-8') as f:
            cmds = json.load(f)
            return cmds
    
    def module_path(self, module_name: str) -> str:
        """
        Returns the path to a specific module within the workspace package.
        """
        return os.path.join(self.path, module_name)
        
    def modules(self) -> list:
        """
        Returns a list of module names (directories) inside the workspace package.
        """
        modules_path = os.path.join(workspaces_packages, self.workspace_type, "modules")
        if not os.path.isdir(modules_path):
            return []
        # List only directories (modules)
        return [d for d in os.listdir(modules_path) if os.path.isdir(os.path.join(modules_path, d))]

        
