import os
import sys

__version__ = "0.1.0"

if sys.platform.startswith("win"):
    workspaces_packages = r"C:\.temple\workspaces"
else:
    workspaces_packages = os.path.join(os.path.expanduser("~"), ".temple", "workspaces")
    