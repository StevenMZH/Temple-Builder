import os
import click
import json

from temple.builder.configs import TempleConfig
from temple.builder.package import WorkspacePackage
from temple.internal.files import file_append, file_insert, file_post, get_filenames, file_create
from temple.internal.runner import run_local
from temple.internal.edition import replace_variables

def run_build(workspace_name: str, workspace_type: str, module: str):
    click.echo(f"Running {workspace_type} {module} build for the {workspace_name} workspace...")
    
    # Templa Update
    config = TempleConfig()
    config.add_workspace(workspace_name, workspace_type)

    # Workspace Build
    pkg = WorkspacePackage(workspace_type)
    run_workspace_cmds(workspace_name, pkg, module)
    run_workspace_actions(workspace_name, pkg, module)


def run_workspace_actions(workspace_name: str, package:WorkspacePackage, module: str, force: bool = False):
    """
    Iterates over the subdirectories of workspaces_packages/{workspace_type}/{module}
    and applies the action corresponding to the subdirectory name (append, post, insert, etc.)
    to each file inside it.
    """
    base_path = package.module_path(module)
    config = TempleConfig().read()
    
    if(config.get('workspaces', {})):
        paths = config.get('workspaces', {}).get(workspace_name, {}). get('build', {})
    else:
        paths = {}

    if not os.path.isdir(base_path):
        print(f"Directory not found: {base_path}")
        return

    for action in os.listdir(base_path):
        action_dir = os.path.join(base_path, action)
        if not os.path.isdir(action_dir):
            continue

        files_in_action = [f for f in os.listdir(action_dir) if os.path.isfile(os.path.join(action_dir, f))]
        if not files_in_action:
            continue

        for filename in files_in_action:
            file_path = os.path.join(action_dir, filename)
            path = replace_variables(paths.get(filename, filename), packages_vars(workspace_name))
            
            target = os.path.join(workspace_name, path)
            root = filename

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    content = replace_variables(content, packages_vars(workspace_name))
                    
                if "__init__" in filename:
                    continue

                if action == "create" or action == "add":
                    file_create(target, content, force)
                elif action == "create_root" or action == "add_root":
                    file_create(root, content, force)
                    
                elif action == "append":
                    file_append(target, content, is_path=False)
                elif action == "append_root":
                    file_append(root, content, is_path=False)
                    
                elif action == "post":
                    file_post(target, content, is_path=False)
                elif action == "post_root":
                    file_post(root, content, is_path=False)
                    
                elif action == "insert":
                    # file_insert(target, None, content)
                    pass
                elif action == "insert_root":
                    # file_insert(root, None, content)
                    pass
                
                # delete
                
                else:
                    print(f"Unknown action: {action}")
            except Exception as e:
                print(f"Error applying '{action}' to {root}: {e}")

def run_workspace_cmds(workspace_name: str, pkg: WorkspacePackage, module: str):
    """Run a module list for the defined workspace module (from filesystem path)"""
    try:
        cmds = pkg.cmds()
        cmd_list = cmds.get(module, [])
        if workspace_name:
            cmd_list = [c.replace("workspace_name", workspace_name) for c in cmd_list]
        run_local(cmd_list)
    except (FileNotFoundError, AttributeError):
        print(f"Command file not found for workspace type: {pkg.workspace_type}")
        return


def packages_vars(workspace_name:str) -> dict:
    vars = {}
    vars["workspace_name"] = workspace_name
    return vars

