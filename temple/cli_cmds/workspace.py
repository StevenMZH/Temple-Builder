import click
from temple.builder.group import setup_group
from temple.builder.workspaces import run_build

@click.command("init")
@click.argument("name")
@click.option('--force', is_flag=True, help="Force overwrite existing files.")
def init(name: str, force: bool):
    """
    Setup init workspace group for a project
    """
    setup_group(name, force=force)
    # LICENSE

    
@click.command("init_workspace")
@click.argument("workspace")
@click.argument("name")
def init_workspace(workspace:str, name:str):
    """
    Setup the specified workspace
    """
    # create or enter venv
    # install dependencies
    # setup template & project strucutre
    # requirements
    # dockerfile
    if(workspace=="all"):
        pass
    else:
        run_build(name, workspace, 'init')
    
@click.command("build")
@click.argument("workspace")
def build(workspace:str):
    """
    Update the workspace based on the build settings
    """
    # create or enter venv
    # install dependencies
    # setup template & project strucutre
    # requirements
    # dockerfile
    if(workspace=="all"):
        pass
    else:
        pass