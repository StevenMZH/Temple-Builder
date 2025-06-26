import click

@click.command("install")
@click.argument("workspace")
def install(workspace: str):
    """
    Install workspace builds/interpreters/modules.
    """
    pass


@click.command("cmd")
@click.argument("workspace")
@click.argument("cmd")
def cmd(workspace: str, cmd: str):
    """
    Run a setup command in the specified workspace.
    """
    pass


@click.command("run")
@click.argument("mode", type=click.Choice(["dev", "prod"]))
def run(mode):
    """Run the workspace group in dev or prod mode"""
    if mode == "dev":
        pass
    elif mode == "prod":
        pass
