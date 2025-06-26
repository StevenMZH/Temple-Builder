import click
from temple import __version__

# Lists    
@click.command("version")
def version():
    """
    temple-builder version
    """
    click.echo(f"temple-builder, version {__version__}")

# Lists    
@click.command("list_workspaces")
def list_workspaces():
    """
    List workpaces builders/interpreters
    """
    
# Lists    
@click.command("about")
@click.argument("workspace")
def about(workspace:str):
    """
    Explain the workspace builders/interpreters/modules/cmds
    """