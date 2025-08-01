import os
from agents import function_tool

@function_tool
def read_file(name: str) -> str:
    """
    Reads a file and returns the content.
    """
    with open(os.path.join('assistant-data', os.path.dirname(__file__), name), "r") as f:
        return f.read()

@function_tool
def write_file(name: str, content: str):
    """
    Writes to a file.
    """
    if not os.path.exists(os.path.join('assistant-data', os.path.dirname(__file__))):
        os.makedirs(os.path.join('assistant-data', os.path.dirname(__file__)))
    with open(os.path.join('assistant-data', os.path.dirname(__file__), name), "w") as f:
        f.write(content)

@function_tool
def append_file(name: str, content: str):
    """
    Appends to a file.
    """
    with open(os.path.join('assistant-data', os.path.dirname(__file__), name), "a") as f:
        f.write(content)

@function_tool
def delete_file(name: str):
    """
    Deletes a file.
    """
    os.remove(os.path.join('assistant-data', os.path.dirname(__file__), name))

@function_tool
def list_files():
    """
    Lists all files in the assistant-data directory.
    """
    return os.listdir(os.path.join('assistant-data', os.path.dirname(__file__)))

