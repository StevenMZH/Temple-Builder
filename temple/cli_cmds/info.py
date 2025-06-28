import os
import click
from temple import __version__, workspaces_packages

# Lists    
@click.command("version")
def version():
    """
    temple-builder version
    """
    click.echo(f"temple-builder, version {__version__}")

# Lists    
@click.command("list")
@click.argument("package", required=False)
@click.option('--all', is_flag=True, help="List official workspace packages ready to be installed")
def list(package:str=None, all:bool=False):
    """
    List workpaces builders/interpreters
    """
    list_path = os.path.join(workspaces_packages, package) if package else workspaces_packages
    if not os.path.isdir(list_path):
        return []
    pkgs = [d for d in os.listdir(list_path) if os.path.isdir(os.path.join(list_path, d))]
    
    click.echo("Available workspace packages locally:") if not package else click.echo(f"Modules from {package} package:") 
    for pkg in pkgs:
        click.echo(f"  - {pkg}")
        
    if all:
        click.echo("\nOfficial workspace packages ready to be installed:")
   
    
@click.command("about")
@click.argument("package", required=False)
@click.option('--all', is_flag=True, help="List official workspace packages ready to be installed")
def about(package: str = None, all: bool = False):
    """
    List workspaces builders/interpreters and show README.md if available.
    """
    list_path = os.path.join(workspaces_packages, package) if package else workspaces_packages

    if package:
        readme_path = os.path.join(list_path, "README.md")
        if os.path.isfile(readme_path):
            click.echo(f"\n--- {package} README.md ---\n")
            with open(readme_path, "r", encoding="utf-8") as f:
                click.echo(f.read())
        else:
            click.echo(f"No README.md found for package '{package}'.")
    else:
        pkgs = [d for d in os.listdir(list_path) if os.path.isdir(os.path.join(list_path, d))]
        click.echo("Available workspace packages locally, select one to see the documentation:")
        for pkg in pkgs:
            click.echo(f"  - {pkg}")

    if all:
        click.echo("\nOfficial workspace packages ready to be installed:")