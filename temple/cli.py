import click
from temple import __version__

from temple.cli_cmds.info import version, list_workspaces, about
from temple.cli_cmds.cmds import install, cmd, run
from temple.cli_cmds.workspace import init, init_workspace, build
from temple.cli_cmds.virtual_env import prompt, virtualize, add_workpace, add_module

@click.group()
@click.version_option(__version__, prog_name="temple-builder")
def cli():
    """Temple - Builder Fullstack CLI"""
    pass

# Info commands
cli.add_command(version)
cli.add_command(list_workspaces)
# cli.add_command(about)

# Workspace commands
cli.add_command(init)
cli.add_command(init_workspace)
cli.add_command(build)

# Virtual env commands
# cli.add_command(prompt)
# cli.add_command(virtualize)
# cli.add_command(add_workpace)
# cli.add_command(add_module)

# Other commands
# cli.add_command(install)
cli.add_command(cmd)
# cli.add_command(run)

def main():
    cli()

if __name__ == "__main__":
    cli()
