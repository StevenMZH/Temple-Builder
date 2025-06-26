import click
from typing import Dict, List
import subprocess

def run_local(commands: List[str]):
    command_str = " && ".join(commands)
    result = subprocess.run(command_str, check=True, capture_output=True, text=True, shell=True)
    click.echo(f"(local): {result.stdout}")
    if result.stderr:
        click.echo(f"(local): {result.stderr}")
  