import click
import os

def replace_variables(content: str, variables: dict) -> str:
    """Replace variables in a string content with the provided values."""
    try:
        for key, value in variables.items():
            content = content.replace(f"{{{{{key}}}}}", str(value))
        return content
    except Exception as e:
        click.echo(f"Error replacing variables in content: {e}")
        return

