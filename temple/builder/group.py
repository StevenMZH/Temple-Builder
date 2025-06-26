from temple.internal.files import file_create
from temple.builder.configs import TempleConfig
from temple.builder.package import WorkspacePackage
from temple.builder.workspaces import run_workspace_actions

def setup_group(name, force: bool = False):
    config = TempleConfig()
    config.init(name, force)

    pkg = WorkspacePackage("temple")
    run_workspace_actions(name, pkg, "init", force)    
    file_create("README.md", f"# {name}\n\n", force)
    
    # LICENSE
    # .dockerignore
