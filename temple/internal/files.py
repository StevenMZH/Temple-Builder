import os
import shutil
import click


def file_create(target, content="", replace=False):
    """
    Create a new file at the target path with the given content.
    If the file already exists and replace is False, do nothing.

    :param target: Destination file path
    :param content: Content to write to the file (default: empty string)
    :param replace: If True, overwrite existing file. If False, do not modify existing file.
    """
    dirpath = os.path.dirname(target)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    if os.path.exists(target) and not replace:
        click.echo(f"{target} already exists (No changes made)")
        return
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
        
    if replace:
        click.echo(f"{target} Overwritten")
    else:
        click.echo(f"{target} Created")
    
def file_post(target, content, is_path=True):
    """
    Write content to a target file. If is_path is True, content is a file path to copy from.
    Otherwise, content is raw string content to write.

    :param target: Destination file path
    :param content: Path to source file OR raw content string
    :param is_path: If True, content is a path. If False, content is plain text
    """
    os.makedirs(os.path.dirname(target), exist_ok=True)

    if is_path:
        shutil.copyfile(content, target)
    else:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

    click.echo(f"{target} Updated")
    
def file_append(target, content, is_path=True):
    """
    Append content to a file. If is_path is True, content is a file path to read from.
    Otherwise, content is a string to append directly.

    :param target: Path to file to append to
    :param content: Path to content file OR string to append
    :param is_path: If True, content is a file path. If False, content is raw text
    """
    dirpath = os.path.dirname(target)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    if is_path:
        with open(content, 'r', encoding='utf-8') as f:
            content_data = f.read()
    else:
        content_data = content

    with open(target, 'a', encoding='utf-8') as f:
        f.write(content_data + '\n')

    click.echo(f"{target} Updated")

def file_insert_value(path, filter, content):
    pass

def file_insert(path, filter, content):
    pass


# Get names
def get_filenames(path):
    """
    Returns a list of file names (not directories) in the given path.
    """
    return [entry.name for entry in os.scandir(path) if entry.is_file()]



