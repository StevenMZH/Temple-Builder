import click

# Temple configs via CMDs for AI
@click.command("prompt")
@click.argument("prompt")
def prompt(prompt):
    """
    Ask AI to help build a project using temple enviroment
    """
    pass

# Virtual env for AI to work in
@click.command("virtualize")
def virtualize():
    """
    Set virtual enviroment for build/interpretate without affecting the actual project
    """
    pass

@click.command("add_workspace")
@click.argument("workspace")
def add_workpace(workspace:str):
    """
    Add no tracked workspace to the temple config
    """
    pass

@click.command("add_module")
@click.argument("workspace")
@click.argument("module")
def add_module(workspace:str, module:str):
    """
    Add a new module to a temple workspace
    """
    pass
    # dockerization 
    # sockets
    # postgres
    # mongo
    # redis