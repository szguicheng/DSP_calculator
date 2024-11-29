import os

def joinpath(*paths: str) -> str:
    '''
    Join paths with the current directory.

    ``*paths``: One or more path fragments.

    Returns:
    str: The joined full path.

    Example:
    >>> joinpath("folder", "subfolder", "file.txt")
    'current_directory/folder/subfolder/file.txt'
    '''
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, *paths)
    return os.path.normpath(full_path)
